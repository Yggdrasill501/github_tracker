"""Module contains urls for the project."""
from django.urls import path
from .views import github_events


urlpatterns = [
    path('events', github_events, name='github_events')
]
