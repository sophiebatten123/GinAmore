'''
Imports relevant django packages
'''
from django.apps import AppConfig


class OurstoryConfig(AppConfig):
    '''
    Generates the ourstory app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'ourstory'
