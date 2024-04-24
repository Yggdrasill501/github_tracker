"""Module contains views for the GitHubEvent model."""
from .models import GitHubEvent
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import GitHubEventSerializer
from .utils.github_api import GitHubApi


class GitHubEventApi(APIView):
    """Class for GitHubEventApi view."""

    def get(self, request):
        """Get the GitHub events.

        :param request: WSGIRequest, request object.
        :return: Response, response object.
        :rtype: Response.
        """
        github_api = GitHubApi()
        repository_name = 'django/django'
        events = github_api.get_events(repository_name)
        return Response(events)


class GitHubEventListCreate(generics.ListCreateAPIView):
    """Class for GitHubEventList view."""

    queryset = GitHubEvent.objects.all()
    serializer_class = GitHubEventSerializer
