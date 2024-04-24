"""Module contatins api for GitHub events."""
import logging
import requests
from django.conf import settings

MODULE_LOGGER = logging.getLogger(__name__)


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
        MODULE_LOGGER.debug('Fetching events for %s', repository_name)
        response = self.session.get(url, params=params)
        if response.status_code == 200:
            MODULE_LOGGER.debug(f'Successfully fetched events for {repository_name}')
        else:
            MODULE_LOGGER.error(f'Failed to fetch events for {repository_name}')
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
        MODULE_LOGGER.debug('Fetching user info for %s', username)  
        if response.status_code == 200:
            MODULE_LOGGER.debug(f'Successfully fetched usr info for {username}')
        else:
            MODULE_LOGGER.error(f'Failed to fetch user info for {username}')
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
