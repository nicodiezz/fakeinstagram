from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models.base import Model as Model
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, RedirectView
from .models import Post, Like, Comment
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import get_object_or_404
# Create your views here.
#Posts
class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "posts/post_detail.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        post = self.get_object()   
        if post.like_set.filter(user=self.request.user).exists():
            context["liked"]= [post.id]
        context['comments'] = post.comment_set.all() 
        return context

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    def get_queryset(self):
        posts = Post.objects.filter(user__in=self.request.user.following.all()).order_by('-created_at')
        return posts
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if "liked" not in context:
            context["liked"]=[]
        for post in self.get_queryset():
            if post.like_set.filter(user=self.request.user).exists():
                context["liked"]+= [post.id]
        return context
        
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/create_post.html"
    fields = ('image','description')
    success_url= reverse_lazy('home')

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        form.instance.user = self.request.user
        if form.is_valid():
            user = self.request.user
            user.posts_count+=1
            user.save()
            messages.success(request,"post created succesfully!")
            return self.form_valid(form)
        else:
            return self.form_invalid(form)     
        
class PostUpdateView(LoginRequiredMixin,UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields= ("description",)
    def form_valid(self, form):
        messages.success(self.request,"post edited succesfully!")
        return super().form_valid(form)
        
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            messages.error(request, "You are not allowed to edit this post")
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
class PostDeleteView(LoginRequiredMixin,DeleteView):
    model = Post
    template_name = "confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["to_delete"] = "this post" 
        return context
    
    def get_success_url(self):
        messages.success(self.request, 'Post deleted successfully')
        return self.get_object().user.get_absolute_url()
    
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            messages.error(request, "You are not allowed to edit this post")
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_valid(self, form):
        user = self.get_object().user
        user.posts_count -= 1
        user.save()
        return super().form_valid(form)

#Likes
class LikeView(LoginRequiredMixin,RedirectView):
    model = Like
    def get_redirect_url(self):
        return self.request.META.get('HTTP_REFERER')
    
    def post(self, request, pk):
        post = get_object_or_404(Post,pk=pk)
        user = request.user
        like,created = Like.objects.get_or_create(post=post, user=user)
        if created:
            like.save()
            post.likes_count+=1
            post.save()
        else:
            post.likes_count-=1
            post.save()
            like.delete()
        return super().post(request)

#Comments
class CommentCreateView(LoginRequiredMixin,CreateView):
    model = Comment
    fields=("text",)
    def get_success_url(self):
        return self.get_object().post.get_absolute_url()
    
    def post(self, request,pk):
        form = self.get_form()
        form.instance.user = self.request.user
        form.instance.post = get_object_or_404(Post,pk=pk)
        if form.is_valid():
            messages.success(request,"Post commented succesfully!")
            return self.form_valid(form)
        else:
            messages.error(request,"Post couldn't be commented")
            return self.form_invalid(form)
        
class CommentDeleteView(LoginRequiredMixin,DeleteView):
    model = Comment
    template_name = "confirm_delete.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["to_delete"] = "this comment" 
        return context
    
    def get_success_url(self):
        return self.get_object().post.get_absolute_url()
    
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            messages.error(request, "You are not allowed to delete this comment")
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
    def form_invalid(self, form):
        messages.success(self.request, "Comment couldn't be deleted")
        return super().form_invalid(form)
    
    def form_valid(self, form):
        messages.success(self.request, 'Comment deleted successfully')
        return super().form_valid(form)