from django.urls import path
from django.utils import timezone
from app import views



urlpatterns = [
    path('', views.hello),
    path('job/<id>', views.job_detail),
    path('job/', views.job_list)
]