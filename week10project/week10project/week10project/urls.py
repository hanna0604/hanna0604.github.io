from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('ccu409220029', views.ccu409220029_function)
]
