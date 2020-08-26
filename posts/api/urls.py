from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework.routers import SimpleRouter
from .views import LikeUnlikeViewSet, PostViewSet

app_name = 'posts'
router = SimpleRouter()
# , basename='MyModel2'
router.register(r'post-list', PostViewSet)

urlpatterns = [
    path('like-unlike/', LikeUnlikeViewSet.as_view(), name='like-unlike-url'),
]

urlpatterns += router.urls
