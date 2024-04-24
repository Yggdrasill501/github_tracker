from django.shortcuts import render
from github_tracker.github_api import GithubApi


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
