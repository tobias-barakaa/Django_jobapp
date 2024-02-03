from django.urls import path
from django.utils import timezone
from app import views



urlpatterns = [
    path('', views.job_list, name='job_home'),
    path('hello/', views.hello, name='hello'),
    path('job/<int:id>', views.job_detail, name='jobs_detail'),
    path('job/<str:id>', views.job_detail)
]