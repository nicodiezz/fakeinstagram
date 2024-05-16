"""
URL configuration for fakeinstagram project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from fakeinstagram.settings import LOCAL_APPS
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('home.urls'))
]

for app in LOCAL_APPS:
    try:
        path(f'{app}/',include(f'{app}.urls'))
    except ModuleNotFoundError:
        pass

from .settings import DEBUG,MEDIA_URL,MEDIA_ROOT
from django.conf.urls.static import static
if DEBUG:
    urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)
