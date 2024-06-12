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
        if 'search_history' in request.session:
            search_history = request.session['search_history']
            context["search_history"] = search_history
        return super().render_to_response(context)
    
    def post(self, request, *args, **kwargs):
        #Get Results
        key = request.POST.get("key")
        users = CustomUser.objects.filter(username__icontains=key)
        context = super().get_context_data(**kwargs)
        context["users"] = users

        #Store history records
        session = request.session
        if "search_history" not in session:
            session["search_history"] = []
        session["search_history"].append(key)
        session.save()
               
        return super().render_to_response(context)
