from djangoproject2 import views
from django.urls import path

from django.contrib import admin
urlpatterns = [
    path("", views.home),
    path("ccu410123456", views.ccu410123456_function),
    path("admin/", admin.site.urls)
]
