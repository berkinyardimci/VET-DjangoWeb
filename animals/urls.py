from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.animal_list, name = 'animals'),
]
