from django.views.generic import FormView, DetailView
from .forms import CustomUserCreationForm 
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from posts.models import Post
# Create your views here.
class SignUpView(FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html" 
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)

#   Para manejo de errores:    
#    def get_context_data(self, **kwargs):
#            context = super().get_context_data(**kwargs)
#            if self.form_class.errors:
#                for field,errors in self.form_class.errors.items():
#                    context[field] = errors
#            return context

class CustomUserDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name = "user_detail.html"
    context_object_name = "user"

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.get_queryset()
        context["posts"] = Post.objects.filter(user_id = user[0].id)
        print(context["posts"])
        return context
    

        
    
    
    

    
