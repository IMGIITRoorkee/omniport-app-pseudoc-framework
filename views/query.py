from rest_framework import generics, permissions

from pseudoc_framework.serializers.query import QueryDetailSerializer
from pseudoc_framework.models import Query


class QueryDetailView(generics.RetrieveAPIView):
    """
    View for query details
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = QueryDetailSerializer
    queryset = Query.objects.all()
