from django.contrib import admin
from django.urls import path

from .views import Complete, Home, Delete, Uncomplete

urlpatterns = [
    path('', Home, name='Home'),
    path('delete/<int:id>', Delete, name='Delete'),
    path('complete/<int:id>', Complete, name='Complete'),
    path('uncomplete/<int:id>', Uncomplete, name='Uncomplete'),
    
]