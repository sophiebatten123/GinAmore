'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Cocktail, CocktailCategory, CocktailIngredient
from django_summernote.admin import SummernoteModelAdmin


class CategoryAdmin(admin.ModelAdmin):
    '''
    Creates admin display in database
    '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(CocktailCategory, CategoryAdmin)


class CocktailIngredientInline(admin.StackedInline):
    '''
    Information to be displayed in the ingredient admin database
    '''
    model = CocktailIngredient
    extra = 0


class CocktailAdmin(admin.ModelAdmin):
    '''
    Information to be displayed in the cocktail admin database
    '''
    inlines = [CocktailIngredientInline]
    list_display = (
        'name',
        'category',
        'rating',
        'image',
    )


admin.site.register(Cocktail, CocktailAdmin)
