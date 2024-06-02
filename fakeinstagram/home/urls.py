from django.urls import path
from . import views 
urlpatterns = [
    path('',views.PostListView.as_view(),name="home"),
    path('search/',views.SearchView.as_view(),name="search")
]
