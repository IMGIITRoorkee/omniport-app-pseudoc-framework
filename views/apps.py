from rest_framework import viewsets, permissions

from new_pseudoc.serializers.apps import (
    AppDetailSerializer,
    AppListSerializer,
)
from new_pseudoc.models import App


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View to list available apps and services in pseudoc
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = AppDetailSerializer
    queryset = App.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return AppDetailSerializer
        else:
            return AppListSerializer
