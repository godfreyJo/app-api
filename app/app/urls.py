from django.contrib import admin
from django.urls import path, include
from rest_framework import routers





urlpatterns = [
    path('', include('restApp.urls')),
    path('admin/', admin.site.urls),
]
