'''
Imports relevant django packages
'''
from django.db import models
from django.contrib.auth.models import User


class CocktailCategory(models.Model):
    '''
    Cockatil category model
    '''
    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        '''
        Returns the categories friendly name
        '''
        return self.friendly_name


class Cocktail(models.Model):
    '''
    Cocktail information model
    '''
    category = models.ForeignKey(
        'CocktailCategory',
        null=True,
        blank=True,
        on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = models.TextField()
    recipe = models.TextField()
    ingredients = models.TextField()
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=False)

    def __str__(self):
        return self.name


class CocktailReview(models.Model):
    '''
    User review model for cocktail recipes
    '''
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    cocktail = models.ForeignKey(Cocktail, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=False, blank=False)
    user_review = models.TextField(max_length=250, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Returns the review as a string
        '''
        return f'{self.title}'
