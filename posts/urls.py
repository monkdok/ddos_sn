"""profiles URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter

from .views import *

app_name = 'posts'
# router = SimpleRouter()
# router.register(r'post-list', PostViewSet)
# router.register(r'test', TestViewSet)


urlpatterns = [
    path('post-list/', PostListView.as_view(), name="post_list_url"),
    path('like-unlike-post/', like_unlike_post, name="like_unlike_post_url"),
]

# urlpatterns += router.urls
