from django.urls import path
from .views import GetNotificationsAPIView, MarkAsReadAPIView

urlpatterns = [
    path('get-notifications/', GetNotificationsAPIView.as_view(), name='get_notifications'),
    path('mark-as-read/<int:notification_id>/', MarkAsReadAPIView.as_view(), name='mark_as_read'),

]
