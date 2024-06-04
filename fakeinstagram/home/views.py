from django.views.generic import ListView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.views import CustomUserDetailView
from posts.models import Post
from users.models import CustomUser
# Create your views here.
class PostListView(LoginRequiredMixin, ListView):
    model = Post
    template_name = "home.html"
    context_object_name = "posts"
    def get_queryset(self,*args, **kwargs):
        posts = Post.objects.filter(user__in=self.request.user.following.all()).order_by('-created_at')
        return posts
    
class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search.html"
    users = None
    def post(self, request, *args, **kwargs):
        key = request.POST.get("key")
        self.users = CustomUser.objects.filter(username__icontains=key)
        context = super().get_context_data(**kwargs)
        context["users"] = self.users
        return super().render_to_response(context)
