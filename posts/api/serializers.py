from rest_framework import serializers
from rest_framework_jwt.compat import Serializer

from ..models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeUnlikeSerializer(Serializer):
    post_id = serializers.IntegerField(min_value=0, max_value=999999)


class PostLikeAnalyticsSerializer(Serializer):
    date_from = serializers.CharField(max_length=100)
    date_to = serializers.CharField(max_length=100)

