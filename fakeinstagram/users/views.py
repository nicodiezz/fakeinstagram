from django.db.models.base import Model as Model
from django.db.models.query import QuerySet
from django.views.generic import FormView, DetailView, RedirectView, UpdateView, DeleteView, ListView
from .forms import CustomUserCreationForm 
from .models import CustomUser
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from posts.models import Post

# Create your views here.
class SignUpView(FormView):
    form_class = CustomUserCreationForm
    template_name = "registration/signup.html" 
    success_url = reverse_lazy("login")
    def form_valid(self, form):
        form.save()
        messages.success(self.request,"Welcome to FakeInstagram")
        return super().form_valid(form)

class FollowView(LoginRequiredMixin,RedirectView):
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

class UnfollowView(LoginRequiredMixin,RedirectView):
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

class CustomUserUpdateView(LoginRequiredMixin,UpdateView):
    model = CustomUser
    template_name = "edit_profile.html"
    fields=('profile_picture','username','first_name','last_name','email','biography','website','birth_date')

    def get_object(self):
        return self.request.user
    def form_valid(self, form):
        messages.success(self.request,"Profile edited succesfully!")
        return super().form_valid(form)

class CustomUserDeleteView(LoginRequiredMixin,DeleteView):
    model = CustomUser
    template_name = "user_confirm_deletion.html"
    success_url = reverse_lazy('signup')

    def get_object(self):
        return self.request.user
    
    def delete(self,request, *args, **kwargs):
        user = self.get_object()
        users = user.following.all()
        for user in users:
            user.followers_count -= 1
            user.save()
        users = user.followers.all()
        for user in users:
            user.following_count -= 1
            user.save()
        messages.success(self.request, 'Profile deleted successfully')
        return super().delete(request,*args, **kwargs)

#   lists
class BaseUserListView(LoginRequiredMixin,ListView):
    model = CustomUser
    template_name = "user_list.html"
    context_object_name = "users"
    def get_user(self):
        user = CustomUser.objects.get(id = self.kwargs['pk'])
        return user
    def get_post(self):
        post = Post.objects.get(id = self.kwargs['pk'])
        return post

class FollowersListView(BaseUserListView):
    def get_queryset(self):
        return self.get_user().followers.all()
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Followers"
        return context
      
class FollowingListView(BaseUserListView):
    def get_queryset(self):
        return self.get_user().following.all()
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Following"
        return context
    
class LikesListView(BaseUserListView):
    def get_queryset(self):
        likes = self.get_post().like_set.all()
        return [like.user for like in likes]
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["list_name"] = "Likes"
        return context
