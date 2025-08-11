from django.urls import path
from .views import AddAlertView, AllAlertsView, UpdateAlertStatusView

urlpatterns = [
    path('add/', AddAlertView.as_view(), name='add-alert'),
    path('all/', AllAlertsView.as_view(), name='all-alerts'),
    path('update-status/', UpdateAlertStatusView.as_view(), name='update-status'),
   
]
