'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Cocktail, Category


class CategoryAdmin(admin.ModelAdmin):
    '''
    Creates admin display in database
    '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)


class CocktailAdmin(admin.ModelAdmin):
    '''
    Information to be displayed in the cocktail admin database
    '''
    list_display = (
        'name',
        'category',
        'rating',
        'image',
    )


admin.site.register(Cocktail, CocktailAdmin)
