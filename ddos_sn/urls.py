from django.conf import settings
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


app_name = 'posts'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    # User Registrations
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    # JWT Authentication
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair_url'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh_pair_url'),
    # Apps
    path('profiles/', include('profiles.urls', namespace='profiles')),
    path('posts/', include('posts.urls', namespace='posts')),
    # Apps API
    path('api/posts/', include('posts.api.urls', 'posts_api')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
User registration:
/auth/users/
request body:
-username
-password

Post create:
/api/posts/
request body:
-content

Post list:
/api/posts/

Post detail:
/api/posts/<int:pk>/


Token generate:
/api/token/
request body:
-username
-password

Token refresh:
/api/token/refresh/ 

Post Like/Unlike:
/api/posts/like-unlike-post/
request body:
-post ID

Post analytics:
/api/posts/like-count/?date_from=2020-08-22 10:00&date_to=2020-08-27 23:00&post_id=26
"""
