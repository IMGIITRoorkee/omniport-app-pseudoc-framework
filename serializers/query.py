from formula_one.serializers.base import ModelSerializer
from pseudoc_framework.models import Query
from pseudoc_framework.serializers.fields import FieldListSerializer


class QueryDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details
    of the query being used in apps in the Pseudoc App
    """
    field_list = FieldListSerializer(read_only=True, many=True)

    class Meta:
        """
        Meta Class for QueryDetailSerializer
        """

        model = Query
        fields = [
            'label',
            'short_description',
            'field_list',
            'app',
        ]
        read_only = [
            'short_description',
            'app'
        ]


class QueryListSerializer(ModelSerializer):
    """
    Serializer for obtaining the list of the queries in apps
    """
    class Meta:
        """
        Meta Class for QueryListSerializer
        """
        model = Query
        fields = [
            'pk',
            'label',
            'short_description'
        ]
        read_only = [
            'label',
            'short_description'
        ]
