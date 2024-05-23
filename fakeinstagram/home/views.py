from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from users.models import CustomUser
# Create your views here.
class PostListView(ListView,LoginRequiredMixin):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class SearchView(TemplateView,LoginRequiredMixin):
    template_name = "search.html"

class ProfileView(TemplateView,LoginRequiredMixin):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(username = "hola")
        context["user"] =  user
        context["posts"] =  Post.objects.all().filter(user_id = user.id)
        return context
    



