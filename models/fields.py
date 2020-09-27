from django.contrib.contenttypes import fields as contenttypes_fields
from django.contrib.contenttypes import models as contenttypes_models
from django.db import models

from formula_one.models.base import Model


class TextField(Model):
    max_length = models.IntegerField(blank=True, default=255)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        max_length = self.max_length
        return f'Text Field: max length = {max_length}'


class NumericField(Model):
    min = models.IntegerField()
    max = models.IntegerField()

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        minimum = self.min
        maximum = self.max
        return f'Numeric Field: min = {minimum}, max = {maximum}'


class Field(Model):
    """
    Model for the fields required in the query
    """
    limit = models.Q(app_label='new_pseudoc', model='textfield') | \
        models.Q(app_label='new_pseudoc', model='numericfield')

    name = models.CharField(
        max_length=63,
        unique=True
    )
    display_name = models.CharField(
        max_length=63,
        unique=True
    )
    desc = models.CharField(
        max_length=255
    )
    required = models.BooleanField(default=True)

    # Relationship with field type entity
    entity_content_type = models.ForeignKey(
        to=contenttypes_models.ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
    )
    entity_object_id = models.PositiveIntegerField()
    entity = contenttypes_fields.GenericForeignKey(
        ct_field='entity_content_type',
        fk_field='entity_object_id',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        name = self.display_name
        return f'{name}'
