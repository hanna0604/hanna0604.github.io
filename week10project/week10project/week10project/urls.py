from week10project import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('confirm', views.confirm)
]
