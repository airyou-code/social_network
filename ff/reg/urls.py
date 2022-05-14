from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test),
    path('', views.singIn, name='singin'),
    
    path('create/', views.newUser)
]
