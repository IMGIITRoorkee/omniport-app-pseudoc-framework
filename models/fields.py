from django.contrib.contenttypes import fields as contenttypes_fields
from django.contrib.contenttypes import models as contenttypes_models
from django.core.exceptions import ValidationError
from django.db import models
import importlib

from formula_one.models.base import Model


class TextField(Model):
    type = 'text'
    max_length = models.IntegerField(blank=True, default=255)
    is_date = models.BooleanField(default=False)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        max_length = self.max_length
        is_date = self.is_date
        return f'Text Field: max length = {max_length}, is_date = {is_date}'


class NumericField(Model):
    type = 'numeric'
    min = models.IntegerField(blank=True, null=True)
    max = models.IntegerField(blank=True, null=True)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        minimum = self.min
        maximum = self.max
        return f'Numeric Field: min = {minimum}, max = {maximum}'

    def clean(self):
        """
        Validation for the max and min values of the model in
        he admin panel.
        """
        minimum = self.min
        maximum = self.max
        if maximum is not None and minimum is not None:
            if minimum > maximum:
                raise ValidationError(
                    'Maximum value can`t be greater than the minimum value.'
                )
            else:
                super().clean()
        else:
            super().clean()


class DropdownField(Model):
    type = 'dropdown'
    function = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    multiple_selection_allowed = models.BooleanField(default=True)

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        function = self.function
        location = self.location
        multiple_selection_allowed = self.multiple_selection_allowed
        return f'Dropdown Field: function = {function}, location = {location},\
            multiple selection allowed = {multiple_selection_allowed} '

    def clean(self):
        """
        Validation for dropdown function for the dropdown
        field in the query.
        """
        try:
            module = importlib.import_module(self.location)
            getattr(module, self.function)
            super().clean()
        except ModuleNotFoundError:
            raise ValidationError('Module not found')
        except AttributeError:
            raise ValidationError('Function not found')


class Field(Model):
    """
    Model for the fields required in the query
    """
    limit = models.Q(app_label='pseudoc_framework', model='textfield') | \
            models.Q(app_label='pseudoc_framework', model='numericfield') | \
            models.Q(app_label='pseudoc_framework', model='dropdownfield')

    name = models.CharField(
        max_length=63,
        unique=True
    )
    display_name = models.CharField(
        max_length=63,
        unique=True
    )
    description = models.CharField(
        max_length=255,
        blank=True,
    )
    required = models.BooleanField(default=True)

    # Relationship with field type entity
    entity_content_type = models.ForeignKey(
        to=contenttypes_models.ContentType,
        on_delete=models.CASCADE,
        limit_choices_to=limit,
    )
    entity_object_id = models.PositiveIntegerField()
    field_attribute = contenttypes_fields.GenericForeignKey(
        ct_field='entity_content_type',
        fk_field='entity_object_id',
    )

    def __str__(self):
        """
        Return the string representation of the model
        :return: the string representation of the model
        """

        field_name = self.display_name
        queries = self.field_query.all()
        if queries.exists():
            query = queries.first()
            app = query.app
            return f'App: {app.name}, ' \
                   f'Query: {query.label}, ' \
                   f'Field: {field_name}'
        else:
            return f'App: , ' \
                   f'Query: , ' \
                   f'Field: {field_name}'
