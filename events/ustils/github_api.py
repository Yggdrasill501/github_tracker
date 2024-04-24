"""Module contatins api for GitHub events."""
import requests
from django.conf import settings


class GithubApi:
    """Api for GitHub events."""

    def __init__(self):
        self.base_url = 'https://api.github.com'
        self.session = requests.Session()
        self.session.headers.update({
            'Authorization': f'token {settings.GITHUB_TOKEN}',
            'Accept': 'application/vnd.github.v3+json',
        })

    def get_events(self, repository_name, per_page=100):
        """Get events for the user.

        :param repository_name: str, name of the repository.
        :param per_page: int, optional, number of events per page.
        :reaise: requests.HTTPError, if the request was unsuccessful.
        :return: list, events for the user.
        :rtype: list
        """
        url = f"{self.base_url}/repos/{repository_name}/events"
        params = {'per_page': per_page}
        response = self.session.get(url, params=params)
        response.raise_for_status()
        return response.json()

    def get_user(self, username):
        """Get user info.

        :param username: str, name of the user.
        :reaise: requests.HTTPError, if the request was unsuccessful.
        :return: dict, user info.
        :rtype: dict
        """
        url = f"{self.base_url}/users/{username}"
        response = self.session.get(url)
        response.raise_for_status()
        return response.json()

    def get_events_for_multiple_repos(self, repos):
        """Get events for multiple repositories.

        :param repos: list, names of the repositories.
        :reaise: requests.HTTPError, if the request was unsuccessful.
        :return: list, events for the user.
        :rtype: list
        """
        events = {}
        for repo in repos:
            events.extend(self.get_events(repo))
        return events
