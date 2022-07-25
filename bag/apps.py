'''
Imports relevant django packages
'''
from django.apps import AppConfig


class BagConfig(AppConfig):
    '''
    App configuration for the bag
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'bag'
