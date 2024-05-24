from django.views.generic import FormView
from .forms import CustomUserCreationForm 
from django.urls import reverse_lazy
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
        
    
    
    

    
