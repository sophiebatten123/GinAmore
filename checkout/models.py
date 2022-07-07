import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from products.models import Product

class Order(models.Model):
    '''
    Creates the users order form
    '''
    order_number = models.CharField(max_length=30, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    country = models.CharField(max_length=50, null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=12, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)


class OrderLineItem(models.Model):
    '''
    Individual item in the shopping bag
    '''
    order = models.ForeignKey(Order, null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems')
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6, decimal_places=2, null=False, blank=False, editable=False)
