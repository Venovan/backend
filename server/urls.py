from django.urls import path
from server import views


urlpatterns = [
    path("profile/<str:roll>", views.fetch_profile),
    path("events", views.fetch_events),
    path("council", views.fetch_council)
]
