from django.contrib.contenttypes import fields as contenttypes_fields
from django.contrib.contenttypes import models as contenttypes_models
from django.db import models

from formula_one.models.base import Model


class TextField(Model):
    value = models.CharField(
        max_length=255
    )


class NumericField(Model):
    value = models.IntegerField()
    min = models.IntegerField()
    max = models.IntegerField()


class Field(Model):
    """
    Model for the fields required in the query
    """
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
    )
    entity_object_id = models.PositiveIntegerField()
    entity = contenttypes_fields.GenericForeignKey(
        ct_field='entity_content_type',
        fk_field='entity_object_id',
    )
