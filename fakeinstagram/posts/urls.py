from django.urls import path
from . import views
posts = [
    path('create/', views.PostCreateView.as_view(), name="create_post"),
    path('post/<pk>', views.PostDetailView.as_view(), name="post_detail"),
    path('edit-post/<pk>', views.PostUpdateView.as_view(), name="update_post"),
    path('delete-post/<pk>', views.PostDeleteView.as_view(), name="delete_post"),
]
from users.views import LikesListView
likes=[
    path('like/<pk>', views.LikeCreateView.as_view(), name="like_post"),
    path('unlike/<pk>', views.LikeDeleteView.as_view(), name="delete_like"),
    path("likes/<pk>", LikesListView.as_view(), name="likes")
]

urlpatterns= posts+likes