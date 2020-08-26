from rest_framework.serializers import ModelSerializer
from .models import Post, Test


class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class TestSerializer(ModelSerializer):
    class Meta:
        model = Test
        fields = '__all__'


