from django.urls import path, include
from rest_framework import routers

from pseudoc_framework.views.apps import AppViewSet
from pseudoc_framework.views.query import QueryDetailView, ExecuteQueryView


app_name = 'pseudoc_framework'

router = routers.SimpleRouter()

router.register(r'apps', AppViewSet, basename='apps')

urlpatterns = [
    path(
        'query/<int:pk>/',
        QueryDetailView.as_view(),
        name='query',
    ),
    path(
        'execute_query/<int:query_pk>/',
        ExecuteQueryView.as_view(),
        name='execute_query',
    ),
    path('', include(router.urls)),
]
