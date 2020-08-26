from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer, LikeUnlikeSerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter
from rest_framework.mixins import RetrieveModelMixin
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from ..models import Post, Like
# from ...profiles.models import Profile
from profiles.models import Profile


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [DjangoFilterBackend, SearchFilter]
    filter_fields = ['content', 'id']
    permission_classes = [IsAuthenticated]


class LikeUnlikeViewSet(APIView):
    def post(self, request):
        serializer = LikeUnlikeSerializer(data=request.data)
        user = request.user
        message = ''
        if serializer.is_valid():
            user_id = serializer.data.get('user_id')
            post_id = serializer.data.get('post_id')
            profile = Profile.objects.get(user=user)
            post = Post.objects.get(id=post_id)

            if profile in post.liked.all():
                post.liked.remove(profile)
            else:
                post.liked.add(profile)

            like, created = Like.objects.get_or_create(user=profile, post_id=post_id)
            if not created:
                if like.value == 'Like':
                    like.value = 'Unlike'
                    message = 'Post Unliked'
                    like.save()
                else:
                    like.value = 'Like'
                    message = 'Post Liked'
                    like.save()
            else:
                like.value = 'Like'
                message = 'Post Liked'
                post.save()
                like.save()
        return Response({'message': message})


class TestList(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/post_list2.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': queryset})


class TestList2(ModelViewSet):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'posts/post_list2.html'

    def get(self, request):
        queryset = Post.objects.all()
        return Response({'posts': queryset})