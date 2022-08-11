'''
Imports relevant django packages
'''
from django.apps import AppConfig


class CocktailsConfig(AppConfig):
    '''
    Generates the cocktails app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'cocktails'
