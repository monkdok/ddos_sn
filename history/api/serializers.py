from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework_jwt.compat import Serializer

from history.models import History


class UserHistorySerializer(ModelSerializer):
    username = serializers.CharField(source='user', read_only=True)
    join_date = serializers.DateTimeField(source='user.date_joined')

    class Meta:
        model = History
        fields = ['username', 'join_date', 'method', 'url', 'date']
