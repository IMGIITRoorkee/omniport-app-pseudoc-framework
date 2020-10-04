from django.urls import path, include
from rest_framework import routers

from new_pseudoc.views.apps import AppViewSet
from new_pseudoc.views.query import QueryDetailView


app_name = 'new_pseudoc'

router = routers.SimpleRouter()

router.register(r'apps', AppViewSet, basename='apps')

urlpatterns = [
    path(
        'query/<int:pk>/',
        QueryDetailView.as_view(),
        name='query',
    ),
    path('', include(router.urls)),
]
