from django.shortcuts import render
from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
from users.models import CustomUser
# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search.html"
    users = None
    def post(self, request, *args, **kwargs):
        key = request.POST.get("key")
        self.users = CustomUser.objects.filter(username__icontains=key)
        context = super().get_context_data(**kwargs)
        context["users"] = self.users
        return super().render_to_response(context)
    

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = "profile.html"
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        context["posts"] =  Post.objects.all().filter(user_id = user.id)
        return context
    



