from django.urls import path
from . import views

urlpatterns = [
    path('', views.sadeness, name='sadeness'),
]