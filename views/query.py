import importlib
from rest_framework import views, generics, permissions
from rest_framework.response import Response
from rest_framework import status

from pseudoc_framework.serializers.query import QueryDetailSerializer
from pseudoc_framework.models import Query


class QueryDetailView(generics.RetrieveAPIView):
    """
    View for query details
    """

    permission_classes = [permissions.IsAuthenticated, ]
    serializer_class = QueryDetailSerializer
    queryset = Query.objects.all()


class ExecuteQueryView(views.APIView):
    """"
    View to handle queries
    """
    permission_classes = [permissions.IsAuthenticated, ]

    def post(self, request, query_pk, format=None):
        try:
            query = Query.objects.get(pk=query_pk)
            module = importlib.import_module(query.query_function_location)
            function = getattr(module, query.query_function)
            response_text = function(data=request.data)
            return Response(data={'message': response_text},
                            status=status.HTTP_200_OK)
        except Query.DoesNotExist:
            return Response(data={'message': 'Bad request'},
                            status=status.HTTP_400_BAD_REQUEST)
