from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    likes = models.ManyToManyField(User, related_name='product_likes', blank=True)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=2000, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name


class Review(models.Model):
    '''
    User review model
    '''
    user = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    title = models.CharField(max_length=25, null=False, blank=False)
    user_review = models.TextField(max_length=250, null=False, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        '''
        Returns the review as a string
        '''
        return f'{self.title}'
