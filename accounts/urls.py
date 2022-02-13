from django.urls import path
from accounts.views import OwnerDetailView
from . import views

urlpatterns = [
    path('owner/<int:pk>', OwnerDetailView.as_view(), name="user_detail"), 

    path('login/', views.user_login, name="login"), 
    path('register/', views.user_register, name="register"), 
    path('dashboard/', views.user_dashboard, name="dashboard"),  
    path('logout/', views.user_logout, name="logout"),    
    path('follow_animal/', views .follow_animal, name="follow_animal"),        
    path('remove_animal/', views .remove_animal, name="remove_animal"),             
]
