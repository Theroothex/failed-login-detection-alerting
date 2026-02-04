from django.urls import path
from . import views

urlpatterns = [
    path("", views.dashboard, name="dashboard"),
    path("events/", views.events, name="events"),
    path("alerts/", views.alerts, name="alerts"),  
]
