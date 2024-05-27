from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView
from .models import Post
from django.urls import reverse_lazy

# Create your views here.
class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    template_name = "create_post.html"
    fields = ('image','description')
    success_url= reverse_lazy('home')

    def post(self, requets, *args, **kwargs):
        form = self.get_form()
        form.instance.user = self.request.user 
        print(form.errors)
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
                
            
    