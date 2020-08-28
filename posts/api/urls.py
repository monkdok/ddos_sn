from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import LikeUnlikeViewSet, PostViewSet, PostLikeAnalytics

app_name = 'posts'
router = SimpleRouter()
router.register(r'post-list-create', PostViewSet)

urlpatterns = [
    path('like-unlike/', LikeUnlikeViewSet.as_view(), name='like-unlike-url'),
    path('like-count/', PostLikeAnalytics.as_view(), name='like-count-url'),
]

urlpatterns += router.urls
