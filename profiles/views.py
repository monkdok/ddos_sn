from django.shortcuts import render
from django.views.generic.base import View
from .models import *


class HomePageView(View):
    def get(self, request):
        profile = Profile.objects.get(user=self.request.user)
        context = {
            'profile': profile
        }
        return render(request, 'home.html', context)