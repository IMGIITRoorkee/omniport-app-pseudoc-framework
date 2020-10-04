from formula_one.serializers.base import ModelSerializer
from new_pseudoc.models import Query
from new_pseudoc.serializers.fields import FieldListSerializer


class QueryDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details
    of the query being used in apps in the Pseudoc App
    """

    class Meta:
        """
        Meta Class for QueryDetailSerializer
        """
        field_list = FieldListSerializer(read_only=True, many=True)

        model = Query
        fields = [
            'label',
            'short_description',
            'field_list',
            'app',
            'api',
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