from django.contrib.auth.models import User
from rest_framework.generics import get_object_or_404
from rest_framework.status import HTTP_400_BAD_REQUEST
from rest_framework.viewsets import ModelViewSet
from .serializers import UserHistorySerializer
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.views.generic import ListView, View
from django.views.generic.detail import SingleObjectMixin
from rest_framework.viewsets import ModelViewSet
from ..models import History


class HistoryViewSet(ModelViewSet):
    serializer_class = UserHistorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = History.objects.all()

    def retrieve(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        instance = History.objects.filter(user=user).latest('date')
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def list(self, request, *args, **kwargs):
        user = User.objects.get(pk=kwargs['pk'])
        queryset = History.objects.filter(user=user)
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)
