from django.db import models

# Create your models here.


class Category(models.Model):

    class Meta:
        verbose_name_plural = "Categories"

    name = models.CharField(max_length=300)
    friendly_name = models.CharField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.name

    def __str__(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=300, null=True, blank=True)
    name = models.CharField(max_length=300)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    image_url = models.URLField(max_length=2000, blank=True, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name
