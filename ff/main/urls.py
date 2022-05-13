from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('registrations/', include('reg.urls'))
]