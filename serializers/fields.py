from formula_one.serializers.base import ModelSerializer
from new_pseudoc.models import Field


class FieldDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details of the fields in a query
    """

    class Meta:
        """
        Meta Class for FieldDetailSerializer
        """

        model = Field
        fields = [
            'pk',
            'name',
            'display_name',
            'description',
            'required',
        ]


class FieldListSerializer(ModelSerializer):
    """
    Serializer for obtaining the list of the of fields
    """
    class Meta:
        """
        Meta Class for FieldListSerializer
        """
        model = Field
        fields = [
            'pk',
            'name',
            'display_name',
            'description'
        ]
        read_only = [
            'name',
            'display_name',
            'description'
        ]