from django.db import models


class Album(models.Model):
    title = models.CharField(
        max_length=255
    )
    description = models.TextField(
        blank=True
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    last_modified_at = models.DateTimeField(
        auto_now=True
    )
