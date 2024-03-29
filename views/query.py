import importlib
from rest_framework import views, generics, permissions
from rest_framework.response import Response
from rest_framework import status

from kernel.permissions.helpcentre import HasHelpcentreRights

from pseudoc_framework.serializers.query import QueryDetailSerializer
from pseudoc_framework.models import Query


class QueryDetailView(generics.RetrieveAPIView):
    """
    View for query details
    """

    permission_classes = [permissions.IsAuthenticated & HasHelpcentreRights, ]
    serializer_class = QueryDetailSerializer
    queryset = Query.objects.all()


class ExecuteQueryView(views.APIView):
    """"
    View to handle queries
    """
    permission_classes = [permissions.IsAuthenticated & HasHelpcentreRights, ]

    def post(self, request, query_pk, format=None):
        try:
            query = Query.objects.get(pk=query_pk)
            module = importlib.import_module(query.query_function_location)
            function = getattr(module, query.query_function)
            response = function(data=request.data)

            # Check if response is a string or tuple
            if isinstance(response, tuple):
                response_data = response[0]
                response_status = response[1]

                # response tuple must be of the form Tuple[str, int]
                if isinstance(response_data, str) and \
                        isinstance(response_status, int):
                    return Response(data=response_data, status=response_status)
                else:
                    return Response(data='Unable to resolve query response',
                                    status=status.HTTP_501_NOT_IMPLEMENTED)

            elif isinstance(response, str):
                return Response(data=response, status=status.HTTP_200_OK)

            else:
                return Response(data='Unable to resolve query response',
                                status=status.HTTP_501_NOT_IMPLEMENTED)

        except Query.DoesNotExist:
            return Response(data='Bad request',
                            status=status.HTTP_400_BAD_REQUEST)
        except IndexError:
            return Response(data='Unable to resolve query response',
                            status=status.HTTP_501_NOT_IMPLEMENTED)
