from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from posts.models import Post
from users.models import CustomUser
# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class SearchView(TemplateView):
    template_name = "search.html"

class ProfileView(TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = CustomUser.objects.get(username = "hola")
        context["user"] =  user
        context["posts"] =  Post.objects.all().filter(user_id = user.id)
        return context
    



