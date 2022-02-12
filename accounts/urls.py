from django.urls import path, include
from accounts.views import OwnerDetailView

urlpatterns = [
    path('owner/<int:pk>', OwnerDetailView.as_view(), name="user_detail"), 

    # path('owner/<int:pk>', OwnerDetailView.as_view(), name="user_detail"), 
    # path('owner/<int:pk>', OwnerDetailView.as_view(), name="user_detail"), 
]
