'''
Imports relevant django packages
'''
from django.urls import path
from . import views

urlpatterns = [
    path('', views.cocktails, name='cocktails'),
    path('<int:product_id>/', views.cocktail_detail, name='cocktail_detail'),
    path('add/', views.add_cocktail, name='add_cocktail'),
    path('edit/<int:product_id>/', views.edit_cocktail, name='edit_cocktail'),
    path(
        'delete/<int:product_id>/',
        views.delete_cocktail,
        name='delete_cocktail'
        ),
    path(
        'delete_cocktail_review/<int:review_id>/',
        views.delete_cocktail_review,
        name='delete_cocktail_review'),
]
