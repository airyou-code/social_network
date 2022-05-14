from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('singin/', include('reg.urls')),
    path('login/', views.login),
    path('logout/', views.logout),
    path('edit/', views.edit),
    path('', views.index),
    path('<int:pk>', views.ls),
]
