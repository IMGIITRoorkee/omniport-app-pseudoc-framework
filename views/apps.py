from rest_framework import viewsets, permissions

from kernel.permissions.helpcentre import HasHelpcentreRights

from pseudoc_framework.serializers.apps import (
    AppDetailSerializer,
    AppListSerializer,
)
from pseudoc_framework.models import App


class AppViewSet(viewsets.ReadOnlyModelViewSet):
    """
    View to list available apps and services in pseudoc
    """

    permission_classes = [permissions.IsAuthenticated & HasHelpcentreRights, ]
    serializer_class = AppDetailSerializer
    queryset = App.objects.all()

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return AppDetailSerializer
        else:
            return AppListSerializer
