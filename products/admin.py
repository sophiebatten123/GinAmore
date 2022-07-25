'''
Imports relevant django packages
'''
from django.contrib import admin
from .models import Product, Category


class CategoryAdmin(admin.ModelAdmin):
    '''
    Creates admin display in database
    '''
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    '''
    Information to be displayed in the product admin database
    '''
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )


admin.site.register(Product, ProductAdmin)
