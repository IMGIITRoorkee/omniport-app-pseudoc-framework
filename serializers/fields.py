from formula_one.serializers.base import ModelSerializer
from new_pseudoc.models.fields import Field, TextField, NumericField, DropdownField
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
            'pk',
            'max_length',
            'type',
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
            'pk',
            'min',
            'max',
            'type',
        ]


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
        else:
            raise Exception('Unexpected Type of Field Provided.')

        return serializer.data


class FieldListSerializer(ModelSerializer):
    """
    Serializer for obtaining the list of the of fields
    """
    field_type = FieldTypeRelatedField(read_only=True)

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
            'field_type',
            'required',
        ]
        read_only = [
            'name',
            'display_name',
            'description'
        ]