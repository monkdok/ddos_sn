from rest_framework  import serializers
from rest_framework_jwt.compat import Serializer

from ..models import Post, Test, Like


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class LikeUnlikeSerializer(Serializer):
    post_id = serializers.IntegerField(min_value=0, max_value=999999)
    user_id = serializers.IntegerField(min_value=0, max_value=999999)
