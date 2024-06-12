from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import BaseModelForm
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import CreateView, DetailView, ListView, UpdateView, DeleteView, RedirectView
from .models import Post,Like
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponseRedirect
# Create your views here.
#Posts
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    def get_queryset(self,*args, **kwargs):
        posts = Post.objects.filter(user__in=self.request.user.following.all()).order_by('-created_at')
        return posts
        
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
class LikeCreateView(LoginRequiredMixin,RedirectView,CreateView):
    model = Like
    def get_redirect_url(self,pk):
        return self.request.META.get('HTTP_REFERER')
    def post(self, request, *args, **kwargs):
        post = Post.objects.get(id=kwargs['pk'])
        user = request.user
        if post and not post.like_set.filter(user=user):
            like = Like.objects.create(post=post, user=user)
            like.save()
            post.likes_count+=1
            post.save()
        return super().post(request, *args, **kwargs)
