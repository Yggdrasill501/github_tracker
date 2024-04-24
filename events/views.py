"""Module for views."""
from django.shortcuts import render
from .utils.github_api import GithubApi
import logging

MODULE_LOGGER = logging.getLogger(__name__)


def github_events(request):
    """Get GitHub events for the user.

    :param request: WSGIRequest, request object.
    :return: HttpResponse, rendered template.
    :rtype: HttpResponse.
    """
    MODULE_LOGGER.info('Fetching GitHub events')
    api = GithubApi()
    repository_name = 'django/django'
    try:
        events = api.get_events(repository_name)
        MODULE_LOGGER.info(f'{len(events)} events fetched')
    except Exception as e:
        MODULE_LOGGER.error('Failed to fetch GitHub events: %s', e)
        events = []

    return render(request, 'github_events.html', {
        'events': events,
        'repository_name': repository_name
        })


def fetch_and_process_github_events():
    """Fetch and process GitHub events.

    :return: None.
    :rtype: None.
    """
    api = GithubApi()
    repos = ['django/django', 'flask/flask', 'rails/rails']
    events = api.get_events_for_multiple_repos(repos)
    for event in events:
        print(event)


def fetch_github_events(request):
    """Fetch GitHub events for the user.

    :param request: WSGIRequest, request object.
    :return: HttpResponse, rendered template.
    :rtype: HttpResponse.
    """
    return render(request, 'github_events.html')
