from django.urls import path
from . import views
urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("profile/<int:pk>",views.CustomUserDetailView.as_view(),name="user_detail"),
    path("profile/<int:pk>/follow/", views.FollowView.as_view(),name="follow"),
    path("profile/<int:pk>/unfollow/", views.UnfollowView.as_view(),name="unfollow"),
]
