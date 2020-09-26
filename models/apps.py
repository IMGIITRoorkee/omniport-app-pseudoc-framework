from django.db import models

from formula_one.models.base import Model


class App(Model):
    """
    This model stores information about apps registered in pseudoc
    """

    name = models.CharField(
        max_length=63,
        unique=True
    )
    short_description = models.CharField(
        max_length=255,
        blank=True,
    )
