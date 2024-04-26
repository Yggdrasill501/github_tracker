from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class GitHubEventAPITests(APITestCase):
    def test_retrieve_events(self):
        url = reverse('github-events')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
