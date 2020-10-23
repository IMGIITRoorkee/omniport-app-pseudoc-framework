from django.urls import path, include
from rest_framework import routers

from pseudoc_framework.views.apps import AppViewSet
from pseudoc_framework.views.query import QueryDetailView
from pseudoc_framework.views.hello_world import HelloWorld

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
        'hello/',
        HelloWorld.as_view(),
        name='query',
    ),
    path('', include(router.urls)),
]
