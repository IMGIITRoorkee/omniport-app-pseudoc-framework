from formula_one.serializers.base import ModelSerializer
from new_pseudoc.serializers.query import QueryDetailSerializer
from new_pseudoc.models import App


class AppDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details
    of the apps being used in the Pseudoc app
    """
    queries = QueryDetailSerializer(read_only=True, many=True)

    class Meta:
        """
        Meta Class for AppListSerializer
        """

        model = App
        fields = [
            'pk',
            'name',
            'short_description',
            'queries'
        ]
        read_only = [
            'short_description'
        ]
