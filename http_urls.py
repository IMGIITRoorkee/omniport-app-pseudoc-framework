from django.urls import path

from new_pseudoc.views.hello_world import HelloWorld

app_name = 'new_pseudoc'

urlpatterns = [
    path('', HelloWorld.as_view(), name='hello_world'),
]
