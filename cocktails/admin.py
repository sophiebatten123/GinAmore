'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Cocktail, Category
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    '''
    Creates admin display in database
    '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)


class CocktailAdmin(SummernoteModelAdmin):
    '''
    Information to be displayed in the cocktail admin database
    '''
    summernote_fields = ('recipe', 'ingredients')

    list_display = (
        'name',
        'category',
        'rating',
        'image',
    )


admin.site.register(Cocktail, CocktailAdmin)
