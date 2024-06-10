from django.urls import path
from . import views 
from posts.views import PostListView
urlpatterns = [
    path('',PostListView.as_view(),name="home"),
    path('search/',views.SearchView.as_view(),name="search")
]
