from django.shortcuts import render
from django.views.generic.base import View
from rest_framework.viewsets import ModelViewSet
from .serializers import ProfileSerializer
from .models import *


class HomePageView(View):
    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        context = {
            'profile': profile
        }
        return render(request, 'profiles/my_profile.html', context)


class ProfileViewSet(ModelViewSet):
        queryset = Profile.objects.all()
        serializer_class = ProfileSerializer
