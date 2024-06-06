from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, UpdateView
from .models import Post
from django.urls import reverse_lazy
from PIL import Image
import os
# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
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
    template_name = "post_detail.html"

class PostUpdateView(UpdateView):
    model = Post
    template_name = "update_post.html"
    fields= ("description",)
