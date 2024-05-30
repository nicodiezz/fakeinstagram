from django.urls import path
from . import views
urlpatterns = [
    path("signup/",views.SignUpView.as_view(),name="signup"),
    path("profile/<pk>",views.CustomUserDetailView.as_view(),name="user_detail"),
]
