from django.views.generic import FormView, DetailView, RedirectView, UpdateView, ListView
from .forms import CustomUserCreationForm 
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin

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

class FollowView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.get(id=user_id)
        return user.get_absolute_url()
    def dispatch(self, request, *args, **kwargs):
        user_to_follow = CustomUser.objects.get(id=kwargs['pk'])
        request.user.following.add(user_to_follow)
        request.user.following_count += 1
        user_to_follow.followers_count += 1
        request.user.save()
        user_to_follow.save()
        return super().dispatch(request,*args, **kwargs)  

class UnfollowView(RedirectView):
    def get_redirect_url(self, *args, **kwargs):
        user_id = kwargs['pk']
        user = CustomUser.objects.get(id=user_id)
        return user.get_absolute_url()
    def dispatch(self, request, *args, **kwargs):
        user_to_unfollow = CustomUser.objects.get(id=kwargs['pk'])
        request.user.following.remove(user_to_unfollow)
        request.user.following_count -= 1
        user_to_unfollow.followers_count -= 1
        request.user.save()
        user_to_unfollow.save()
        return super().dispatch(request,*args, **kwargs)
        
#CRUD

class CustomUserDetailView(LoginRequiredMixin,DetailView):
    model = CustomUser
    template_name = "user_detail.html"
    context_object_name = "user"

    def get_queryset(self):
        return CustomUser.objects.filter(id=self.kwargs['pk'])
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #get posts:
        user = self.get_object()
        context["posts"] = user.post_set.all().order_by('-created_at')

        #check if user is followed by session user
        if self.request.user.following.filter(id = user.id):
            context["following"] = True
        return context

class CustomUserUpdateView(UpdateView):
    model = CustomUser
    template_name = "edit_profile.html"
    fields=('profile_picture','username','first_name','last_name','email','biography','website','birth_date')

    def get_object(self):
        return self.request.user

#   lists
class BaseUserListView(ListView):
    model = CustomUser
    template_name = "user_list.html"