'''
Imports relevant django packages
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
]
