from django.urls import path

from . import views

urlpatterns = [
    path('<str:payload>', views.index, name='index'),
]