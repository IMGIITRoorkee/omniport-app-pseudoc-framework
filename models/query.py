import importlib
from django.db import models
from django.core.exceptions import ValidationError

from formula_one.models.base import Model
from pseudoc_framework.models import Field, App


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
    query_function_location = models.CharField(max_length=255)
    query_function = models.CharField(max_length=255)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        label = self.label
        app = self.app

        return f'app: {app.name}, query: {label}'

    def clean(self):
        """
        Validation for query function to execute on query submission
        """
        try:
            module = importlib.import_module(self.query_function_location)
            getattr(module, self.query_function)
            super().clean()
        except ModuleNotFoundError:
            raise ValidationError('Module not found')
        except AttributeError:
            raise ValidationError('Function not found')
