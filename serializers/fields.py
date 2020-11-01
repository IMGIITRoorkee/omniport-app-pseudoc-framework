import importlib

from formula_one.serializers.base import ModelSerializer
from pseudoc_framework.models import (
    Field,
    TextField,
    NumericField,
    DropdownField
)
from rest_framework import serializers


class TextFieldSerializer(ModelSerializer):
    """
    Serializer for TextField
    """

    class Meta:
        """
        Meta class for TextFieldSerializer
        """
        model = TextField
        fields = [
            'type',
            'pk',
            'max_length',
            'is_date',
        ]


class NumericFieldSerializer(ModelSerializer):
    """
    Serializer for NumericField
    """

    class Meta:
        """
        Meta class for NumericFieldSerializer
        """
        model = NumericField
        fields = [
            'type',
            'pk',
            'min',
            'max',
        ]


class DropdownFieldSerializer(ModelSerializer):
    """
    Serializer for dropdown field
    """
    choices = serializers.SerializerMethodField()

    class Meta:
        """
            Meta class for DropdownFieldSerializer
        """
        model = DropdownField
        fields = [
            'type',
            'multiple_selection_allowed',
            'choices',
        ]

    def get_choices(self, obj):
        module = importlib.import_module(obj.location)
        function = getattr(module, obj.function)
        return function()


class FieldTypeRelatedField(serializers.RelatedField):
    """

    """

    def to_representation(self, value):
        """
        Serialize the fieldType instances using instances of the models
        """
        if isinstance(value, TextField):
            serializer = TextFieldSerializer(value)
        elif isinstance(value, NumericField):
            serializer = NumericFieldSerializer(value)
        elif isinstance(value, DropdownField):
            serializer = DropdownFieldSerializer(value)
        else:
            raise Exception('Unexpected Type of Field Provided.')

        return serializer.data


class FieldListSerializer(ModelSerializer):
    """
    Serializer for obtaining the list of the of fields
    """
    field_attribute = FieldTypeRelatedField(read_only=True)

    class Meta:
        """
        Meta Class for FieldListSerializer
        """
        model = Field
        fields = [
            'pk',
            'name',
            'display_name',
            'description',
            'field_attribute',
            'required',
        ]
        read_only = [
            'name',
            'display_name',
            'description'
        ]
