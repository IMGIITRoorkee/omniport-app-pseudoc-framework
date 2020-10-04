from formula_one.serializers.base import ModelSerializer
from new_pseudoc.models import Query


class QueryDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details
    of the query being used in apps in the Pseudoc App
    """

    class Meta:
        """
        Meta Class for QueryDetailSerializer
        """

        model = Query
        fields = [
            'label',
            'short_description',
            'fields',
            'app',
            'api',
        ]
        read_only = [
            'short_description',
            'app'
        ]
