import os
import uuid

from django.contrib.auth.models import User
from django.db import models


def photo_upload(instance, filename):
    """Gives a unique path to the saved photo in models.
    Arguments:
        instance: the photo itself, it is not used in this
                  function but it's required by django.
        filename: the name of the photo sent by user, it's
                  used here to get the format of the file.
    Returns:
        The unique path that the file will be stored in the DB.
    """

    return 'users/{0}.{1}'.format(uuid.uuid4().hex, os.path.splitext(filename))


class UserProfileModel(models.Model):
    """The Model of the User Profile."""

    account = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    profile_photo = models.ImageField(upload_to=photo_upload)

    def __str__(self):
        return self.account.username


class TodoGroupModel(models.Model):
    """The Model of the Todo Categories."""

    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, related_name='todo_groups')
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title


class TodoModel(models.Model):
    """The Model of the Todo item."""

    category = models.OneToOneField(TodoGroupModel, on_delete=models.CASCADE, related_name='todos')
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title
