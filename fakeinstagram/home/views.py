from typing import Any
from django.http import HttpRequest
from django.http.response import HttpResponse as HttpResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from users.models import CustomUser
# Create your views here.    
class SearchView(LoginRequiredMixin, TemplateView):
    template_name = "search.html"
    def get(self, request, *args, **kwargs):
        context = super().get_context_data(**kwargs)
        search_history = request.session.session_data.get_decoded()['search_history']
        if search_history:
            context["search_history"] = search_history
        return super().render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        #Get Results
        key = request.POST.get("key")
        users = CustomUser.objects.filter(username__icontains=key)
        context = super().get_context_data(**kwargs)
        context["users"] = users
        #Store history records
        data = request.session.session_data.get_decoded()
        if "search_history" not in data:
            data["search_history"] = []
        data["search_history"].append(key)
                
        return super().render_to_response(context)
