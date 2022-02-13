from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.animal_list, name = 'animals'),
    path('<slug:type_slug>/<int:animal_id>', views.animal_detail, name="animal_detail"), 
    path('type/<slug:type_slug>', views.animal_list, name="animals_by_type"), 
    path('genus/<slug:genus_slug>', views.animal_list, name="animals_by_genus"),
    path('search', views.search, name="search"), 

    path('create_animal', views.create_animal, name="create_animal"),   

]
