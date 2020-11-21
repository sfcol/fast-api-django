from django.db import models
from django.conf import settings


class Item(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="items"
    )

class User(models.Model):
    name = models.CharField(max_length=32)
    email = models.CharField(max_length=32)