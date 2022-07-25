'''
Imports relevant django packages
'''
from django.apps import AppConfig


class ProductsConfig(AppConfig):
    '''
    Generates the products app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'products'
