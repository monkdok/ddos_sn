from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, LikeUnlikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Post, Like
from profiles.models import Profile


# List and Create
class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['content', 'id']
    permission_classes = [IsAuthenticated]


# Number of likes on the selected post
class PostLikeAnalytics(APIView):
    def get(self, request):
        date_from = self.request.query_params.get('date_from')
        date_to = self.request.query_params.get('date_to')
        post_id = self.request.query_params.get('post_id')
        post = Post.objects.get(id=post_id)
        post_likes = Post.objects.filter(id=post_id, like__value='Like')
        likes_num = Like.objects.filter(post=post, created__range=(date_from, date_to)).count()
        all_likes_num = Like.objects.filter(created__range=(date_from, date_to)).count()
        return Response({'likes count': likes_num})


class LikeUnlikeViewSet(APIView):
    def post(self, request):
        serializer = LikeUnlikeSerializer(data=request.data)
        user = request.user
        message = ''
        if serializer.is_valid():
            post_id = serializer.data.get('post_id')
            profile = Profile.objects.get(user=user)
            post = Post.objects.get(id=post_id)

            if profile in post.liked.all():
                post.liked.remove(profile)
            else:
                post.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post=post)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                    message = f'Post "{post.content[:20]}" Unliked'
                    like.save()
                else:
                    like.value = 'Like'
                    message = f'Post "{post.content[:20]}" Liked'
                    like.save()
            else:
                like.value = 'Like'
                message = f'Post "{post.content[:20]}" Liked'
                post.save()
                like.save()
        return Response({'message': message})
