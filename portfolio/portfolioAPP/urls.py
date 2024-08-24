from django.urls import path
from .import views

urlpatterns = [
    path('',views.home, name = "HomePage"),
    path('sendemail/', views.email, name ="sendemail"),
    
]
