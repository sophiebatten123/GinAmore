'''
Imports relevant django packages
'''
from django.apps import AppConfig


class WishlistConfig(AppConfig):
    '''
    Generates the wishlist app
    '''
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'wishlist'
