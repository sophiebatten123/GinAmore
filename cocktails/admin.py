'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import (
    Cocktail,
    CocktailCategory,
    CocktailIngredient,
    CocktailRecipeStep
)


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


class CocktailStepInline(admin.TabularInline):
    '''
    Information to be displayed in the steps admin database
    '''
    model = CocktailRecipeStep
    extra = 0


class CocktailAdmin(admin.ModelAdmin):
    '''
    Information to be displayed in the cocktail admin database
    '''
    inlines = [CocktailIngredientInline, CocktailStepInline]
    list_display = (
        'name',
        'category',
        'rating',
        'image',
    )


admin.site.register(Cocktail, CocktailAdmin)
