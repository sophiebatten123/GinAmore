'''
Imports relevant django packages
'''
from django.apps import AppConfig


class ProfilesConfig(AppConfig):
    '''
    Generates the profiles app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'profiles'
