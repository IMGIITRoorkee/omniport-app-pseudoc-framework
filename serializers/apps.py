from formula_one.serializers.base import ModelSerializer
from new_pseudoc.serializers.query import QueryListSerializer
from new_pseudoc.models import App


class AppDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details
    of the apps being used in the Pseudoc app
    """
    queries = QueryListSerializer(read_only=True, many=True)

    class Meta:
        """
        Meta Class for AppDetailSerializer
        """

        model = App
        fields = [
            'pk',
            'name',
            'short_description',
            'queries'
        ]
        read_only = [
            'name',
            'short_description',
        ]


class AppListSerializer(ModelSerializer):
    """
    Serializer for obtaining the list of apps being used in the Pseudoc app
    """
    class Meta:
        """
        Meta Class for AppListSerializer
        """

        model = App
        fields = [
            'pk',
            'name',
            'short_description'
        ]
        read_only = [
            'short_description',
            'name'
        ]
