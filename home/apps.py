'''
Imports relevant django packages
'''
from django.apps import AppConfig


class HomeConfig(AppConfig):
    '''
    Generates the home app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'home'
