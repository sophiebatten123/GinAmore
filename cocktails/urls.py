'''
Imports relevant django packages
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktails, name='cocktails'),
    path('<product_id>', views.cocktail_detail, name='cocktail_detail'),
]
