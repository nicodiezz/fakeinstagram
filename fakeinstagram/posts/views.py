from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView, RedirectView
from .models import Post
from django.urls import reverse_lazy
from django.contrib import messages
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect
# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "posts/create_post.html"
    fields = ('image','description')
    success_url= reverse_lazy('home')

    def post(self, requets, *args, **kwargs):
        form = self.get_form()
        form.instance.user = self.request.user
        if form.is_valid():
            user = self.request.user
            user.posts_count+=1
            user.save()
            return self.form_valid(form)
        else:
            return self.form_invalid(form)     
        
class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    template_name = "posts/update_post.html"
    fields= ("description",)
    def dispatch(self, request, *args, **kwargs):
        if request.user != self.get_object().user:
            messages.error(request, "You are not allowed to edit this post")
            return HttpResponseRedirect(reverse_lazy('home'))
        return super().dispatch(request, *args, **kwargs)
    
class PostDeleteView(DeleteView):
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
        print(f"--------- posts = {user.posts_count}")
        user.posts_count -= 1
        print(f"--------- posts actualizados = {user.posts_count}")
        user.save()
        return super().form_valid(form)
