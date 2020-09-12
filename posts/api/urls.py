from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from .views import PostViewSet, LikeViewSet

app_name = 'posts'

post_create = PostViewSet.as_view({
    'post': 'create'
})
post_list = PostViewSet.as_view({
    'get': 'list'
})
post_detail = PostViewSet.as_view({
    'get': 'retrieve'
})
post_update = PostViewSet.as_view({
    'get': 'retrieve',
    'put': 'update'
})
likes_list = LikeViewSet.as_view({
    'get': 'list',
})
like_unlike = LikeViewSet.as_view({
    'post': 'create'
})
like_analytics = LikeViewSet.as_view({
    'get': 'list'
})


urlpatterns = format_suffix_patterns([
    path('post-create/', post_create, name='post-create-url'),
    path('post-list/', post_list, name='post-list-url'),
    path('post-detail/<int:pk>/', post_detail, name='post-detail-url'),
    path('post-update/<int:pk>/', post_update, name='post-update-url'),
    path('like-list/', likes_list, name='like-list-url'),
    path('like-unlike/', like_unlike, name='like-unlike-url'),
    path('like-analytics/', like_analytics, name='like-analytics-url'),
])

