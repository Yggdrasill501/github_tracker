"""Module for the GitHubEvent model."""
from django.db import models
import logging

MODULE_LOGGER = logging.getLogger(__name__)


class GitHubEvent(models.Model):
    """Model for GitHubEvent."""
    event_type = models.CharField(max_length=255)

