from django.shortcuts import render
from django.views.generic.base import View
from .models import *


class HomePageView(View):
    def get(self, request):
        user = Profile.objects.get(user=self.request.user)
        context = {
            'user': user
        }
        return render(request, 'ddos/home.html', context)