from django.urls import path
from ..views import ProfileCreateView

app_name = 'profiles'

urlpatterns = [
    path("all-profiles", ProfileCreateView.as_view(), name="profile-create"),
]
