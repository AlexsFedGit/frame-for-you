from django.db import models


class Order(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    name = models.CharField(
        max_length=100
    )
    contact = models.CharField(
        max_length=100
    )
    message = models.TextField(
        blank=True
    )
    is_confirmed = models.BooleanField(
        default=False
    )
