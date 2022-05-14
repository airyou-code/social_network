from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('registrations/', include('reg.urls')),
    path('', views.index),
    path('<int:pk>', views.ls),
]
