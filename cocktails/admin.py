'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Cocktail, Category


admin.site.register(Cocktail)
admin.site.register(Category)
