'''
Imports relevant django packages
'''
from django.db import models
from django.contrib.auth.models import User
from .validators import validate_measurements


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
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=False, blank=False)

    @property
    def get_image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
        else:
            return "{% static images/user.PNG %}"

    def __str__(self):
        return self.name


class CocktailIngredient(models.Model):
    '''
    Model to create an ingredient for the recipe
    '''
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
        related_name='cocktail_ingredients_list'
        )
    name = models.CharField(max_length=254)
    quantity = models.CharField(max_length=54)
    measurement = models.CharField(
        max_length=54,
        validators=[validate_measurements]
        )

    def __str__(self):
        return f'{self.name} {self.quantity}{self.measurement}'


class CocktailRecipeStep(models.Model):
    '''
    Model to create the steps for the cocktail recipes
    '''
    cocktail = models.ForeignKey(
        Cocktail,
        on_delete=models.CASCADE,
        related_name='cocktail_steps_list'
        )
    step = models.CharField(max_length=254)

    def __str__(self):
        return self.step


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
