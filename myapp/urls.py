from django.urls import path
from . import views

urlpatterns = [
    path('first/', views.my_app),
    path('home/', views.index, name='index'),
    
]