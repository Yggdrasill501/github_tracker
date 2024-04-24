"""Module for GitHubEvent serializer."""
from rest_framework import serializers
from .models import GitHubEvent
import logging

MODULE_LOGGER = logging.getLogger(__name__)


class GitHubEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = GitHubEvent
        fields = '__all__'
