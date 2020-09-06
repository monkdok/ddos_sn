from .yasg import urlpatterns as doc_urls
from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
import track_actions

app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # The Browsable API  login page
    path('api-auth/login/', include('rest_framework.urls')),

    # User Registrations
    path('auth/', include('djoser.urls')),
    # path('auth/', include('djoser.urls.authtoken')),

    # JWT Authentication
    path('auth/api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair_url'),
    path('auth/api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair_url'),
    # Apps
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    # Apps API
    path('api/posts/', include('posts.api.urls', 'posts_api')),
    path('track_actions/', include('track_actions.urls')),
]

urlpatterns += doc_urls

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
User Registration:
auth/users/
request body:
-username
-password

Token Generation:
auth/api/token/
request body:
-username
-password

Token refresh:
auth/api/token/refresh/ 

Post Create:
api/posts/post-create/
request body:
-content

Post List:
api/posts/post-list/

Post Detail:
api/posts/post-detail/{post_id}

Post Update:
api/posts/post-update/{post_id}

Likes List:
api/posts/like-list/

Post Like/Unlike:
/api/posts/like-unlike/
request body:
-post ID

Post Analytics:
api/posts/like-analytics/

User Activity:
track_actions/history/{user_id}
"""
