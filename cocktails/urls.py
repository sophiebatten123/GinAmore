'''
Imports relevant django packages
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktails, name='cocktails'),
    path('<int:product_id>/', views.cocktail_detail, name='cocktail_detail'),
    path('add/', views.add_cocktail, name='add_cocktail'),
]
