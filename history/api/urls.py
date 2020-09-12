from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from history.api.views import HistoryViewSet

app_name = 'history'

history_detail = HistoryViewSet.as_view({
    'get': 'retrieve'
})

history_list = HistoryViewSet.as_view({
    'get': 'list'
})


urlpatterns = format_suffix_patterns([
    # path('<int:pk>/', history_detail, name='history-detail-url'),
    path('<int:pk>/', history_list, name='history-list-url'),
    path('last-request/<int:pk>/', history_detail, name='history-detail-url'),
])

