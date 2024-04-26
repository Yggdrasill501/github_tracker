"""Module contains urls for the api."""
from django.urls import path
from .views import GithubEventsListCreate, GitHubEventsApi

urlpatterns = [
        path('events/', GithubEventsListCreate.as_view(), name='events-list-create'),
        path('github-events/', GitHubEventsApi.as_view(), name='github-events')
        ]
