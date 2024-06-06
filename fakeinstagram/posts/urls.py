from django.urls import path
from . import views
urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name="create_post"),
    path('post/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('edit-post/<pk>', views.PostUpdateView.as_view(), name="update_post"),
]
