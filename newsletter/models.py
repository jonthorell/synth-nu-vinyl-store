"""
Models for Newsletter App.
"""

from django.db import models

class subscription(models.Model):
    """Model for Subscription object"""

    email = models.EmailField(
        unique=True,
    )

    def __str__(self):
        return str(self.email)