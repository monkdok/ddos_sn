from django.urls import path
from rest_framework.routers import SimpleRouter

from .api.views import PostViewSet
from .views import PostListView, like_unlike_post

app_name = 'posts'
router = SimpleRouter()
router.register(r'post-list', PostViewSet)


urlpatterns = [
    path('post-list/', PostListView.as_view(), name="post_list_url"),
    path('like-unlike-post/', like_unlike_post, name="like_unlike_post_url"),

]

urlpatterns += router.urls
