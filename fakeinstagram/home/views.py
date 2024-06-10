from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
# Create your views here.    
class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search.html"
    users = None
    def post(self, request, *args, **kwargs):
        key = request.POST.get("key")
        self.users = CustomUser.objects.filter(username__icontains=key)
        context = super().get_context_data(**kwargs)
        context["users"] = self.users
        return super().render_to_response(context)
