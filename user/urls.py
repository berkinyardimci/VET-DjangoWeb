from django.urls import path, include
from user.views import TeacherDetailView

urlpatterns = [
    path('owner/<int:pk>', TeacherDetailView.as_view(), name="user_detail"), 

]
