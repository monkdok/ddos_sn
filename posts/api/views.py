from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, LikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from ..models import Post, Like
from profiles.models import Profile
from .service import LikeFilter
from track_actions.requestMiddleware import RequestMiddleware
from history.mixins import ObjectViewMixin


class PostViewSet(ObjectViewMixin, ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    current_request = RequestMiddleware.get_request_data()[1]
    model = Post

    def perform_create(self, serializer):
        user = get_object_or_404(Profile, user=self.request.user)
        serializer.save(author=user)


class LikeViewSet(ObjectViewMixin, ModelViewSet):
    current_request = RequestMiddleware.get_request_data()[1]
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = LikeFilter
    model = Like

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        user = request.user
        message = ''
        if serializer.is_valid(raise_exception=True):
            post_id = serializer.data.get('post')
            profile = get_object_or_404(Profile, user=user)
            post = get_object_or_404(Post, id=post_id)

            if profile in post.liked.all():
                post.liked.remove(profile)
            else:
                post.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post=post)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                    message = 'Unliked'
                    like.save()
                else:
                    like.value = 'Like'
                    message = 'Liked'
                    like.save()
            else:
                like.value = 'Like'
                message = 'Liked'
                post.save()
                like.save()
            return Response({
                'post_id': post_id,
                'post_content': post.content[:20],
                'message': message
            })
        return Response(status=HTTP_400_BAD_REQUEST)

