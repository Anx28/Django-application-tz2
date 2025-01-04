from django.urls import path
from .views import app_healthcheck

urlpatterns = [
    path('healthcheck/', app_healthcheck, name='app_healthcheck'),
]
