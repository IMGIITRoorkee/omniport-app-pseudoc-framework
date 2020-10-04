from formula_one.serializers.base import ModelSerializer
from new_pseudoc.serializers import QueryDetailSerializer
from new_pseudoc.models import App


class AppDetailSerializer(ModelSerializer):
    """
    Serializer for obtaining the details of the apps being used in the Pseudoc app
    """
    query = QueryDetailSerializer(read_only=True, many=True)

    class Meta:
        """
        Meta Class for AppListSerializer
        """

        model = App
        fields = [
            'pk',
            'name',
            'short_description',
            'query'
        ]
        read_only = [
            'short_description'
        ]
