from rest_framework import generics, permissions

from new_pseudoc.serializers.query import QueryDetailSerializer
from new_pseudoc.models import Query


class QueryDetailView(generics.RetrieveAPIView):
    """
    View for query details
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = QueryDetailSerializer
    queryset = Query.objects.all()
