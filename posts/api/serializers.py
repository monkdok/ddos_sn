from django_filters import DateFilter, DateRangeFilter
from rest_framework import serializers
from rest_framework_jwt.compat import Serializer

from ..models import Post, Like


class LikeSerializer(serializers.ModelSerializer):
    user_reacted = serializers.CharField(source='user.user', read_only=True)
    post_author = serializers.CharField(source='post.author.user', read_only=True)
    created = serializers.DateTimeField(source='post.created', format="%Y-%m-%d", read_only=True)
    # created = serializers.CharField(source='created', read_only=True)
    likes_count = serializers.ReadOnlyField(source='post.num_likes')
    content = serializers.CharField(source='post.content', read_only=True)
    liked_by = serializers.PrimaryKeyRelatedField(source='post.liked', read_only=True, many=True)

    class Meta:
        model = Like
        fields = [ 'post', 'post_author', 'created', 'content', 'likes_count', 'liked_by', 'user_reacted']


class PostSerializer(serializers.ModelSerializer):
    # Passing username to the field 'author' instead of user.id
    author = serializers.CharField(source='author.user', read_only=True)
    # author = serializers.SlugRelatedField(slug_field='author.user', read_only=True)
    content = serializers.CharField()
    liked = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    class Meta:
        model = Post
        fields = '__all__'


class PostLikeAnalyticsSerializer(Serializer):
    date_from = serializers.CharField(max_length=100)
    date_to = serializers.CharField(max_length=100)

