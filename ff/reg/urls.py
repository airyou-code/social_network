from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    # path('', views.test),
    path('', views.reg, name='login'),
    path('create/', views.newUser)
]
