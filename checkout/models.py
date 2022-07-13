'''
Imports relevant packages
'''
import uuid

from django.db import models
from django.db.models import Sum
from django.conf import settings

from django_countries.fields import CountryField

from products.models import Product
from profiles.models import UserProfile


class Order(models.Model):
    '''
    Creates the users order form
    '''
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True,
                                     related_name='orders')
    order_number = models.CharField(max_length=30, null=False, editable=False)
    full_name = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    email = models.EmailField(max_length=250, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    town_or_city = models.CharField(max_length=50, null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    street_address1 = models.CharField(max_length=100, null=False, blank=False)
    street_address2 = models.CharField(max_length=100, null=True, blank=True)
    county = models.CharField(max_length=100, null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6,
                                        decimal_places=2,
                                        null=False,
                                        default=0)
    order_total = models.DecimalField(max_digits=12,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    grand_total = models.DecimalField(max_digits=6,
                                      decimal_places=2,
                                      null=False,
                                      default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(
        max_length=254, null=False, blank=False, default='')

    def _generate_order_number(self):
        '''
        Generates a unique and random order number using UUID
        '''
        return uuid.uuid4().hex.upper()

    def update_total(self):
        '''
        Updates the total each time an items is added, updating
        the delivery costs.
        '''
        self.order_total = self.lineitems.aggregate(
            Sum('lineitem_total'))['lineitem_total__sum'] or 0
        if self.order_total < settings.FREE_DELIVERY_THRESHOLD:
            self.delivery_cost = self.order_total * \
                settings.STANDARD_DELIVERY_PERCENTAGE/100
        else:
            self.delivery_cost = 0
        self.grand_total = self.order_total + self.delivery_cost
        self.save()

    def save(self, *args, **kwargs):
        '''
        Override the saving method and sets the order number
        '''
        if not self.order_number:
            self.order_number = self._generate_order_number()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.order_number


class OrderLineItem(models.Model):
    '''
    Individual item in the shopping bag
    '''
    order = models.ForeignKey(Order,
                              null=False,
                              blank=False,
                              on_delete=models.CASCADE,
                              related_name='lineitems')
    product = models.ForeignKey(Product,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    quantity = models.IntegerField(null=False, blank=False, default=0)
    lineitem_total = models.DecimalField(max_digits=6,
                                         decimal_places=2,
                                         null=False,
                                         blank=False,
                                         editable=False)

    def save(self, *args, **kwargs):
        '''
        Override the saving method for the lineitem total
        '''
        self.lineitem_total = self.product.price * self.quantity
        super().save(*args, **kwargs)

        def __str__(self):
            return f'SKU {self.product.sku} on order {self.order.order_number}'
