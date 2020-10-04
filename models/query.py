from django.db import models

from formula_one.models.base import Model
from new_pseudoc.models import Field, App


class Query(Model):
    """
        Model to store app queries
    """

    label = models.CharField(
        max_length=63,
        unique=True,
    )
    short_description = models.CharField(
        max_length=127,
        blank=True,
        null=True,
    )
    field_list = models.ManyToManyField(
        to=Field,
        related_name='field_query',
        blank=True,
    )
    app = models.ForeignKey(
        to=App,
        on_delete=models.CASCADE,
        related_name='queries',
    )
    api = models.URLField()

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        label = self.label
        app = self.app

        return f'app: {app.name}, query: {label}'
