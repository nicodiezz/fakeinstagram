from django.views.generic import FormView
from django.contrib.auth.forms import UserCreationForm 
# Create your views here.
class SignUpView(FormView):
    form_class = UserCreationForm 

    
