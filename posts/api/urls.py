
from django.urls import path, include
from rest_framework.routers import SimpleRouter
from .views import PostViewSet, LikeViewSet

app_name = 'posts'
router = SimpleRouter()
router.register('', PostViewSet)

likes_list = LikeViewSet.as_view({
    'get': 'list',
    'post': 'create'
})

# router.register('like/', likes_list)
urlpatterns = [
    path('like-unlike/', likes_list, name='like-unlike-url'),
    path('', include(router.urls)),
]

urlpatterns += router.urls
