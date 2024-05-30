from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.views import CustomUserDetailView
from posts.models import Post
# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"

class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search.html"

class ProfileView(CustomUserDetailView):
    template_name = "profile.html"
    def get_queryset(self):
        id = self.request.user.id
        self.kwargs["pk"] = id
        return super().get_queryset()
        
    



