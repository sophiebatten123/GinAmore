from django.contrib import admin
from .models import Order, OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    readonly_fields = ('order_number',
                       'delivery_cost',
                       'order_total',
                       'grand_total',
                       'date',)
                       
    fields = ('full_name',
              'order_number',
              'date',
              'phone_number',
              'country',
              'email',
              'postcode',
              'town_or_city',
              'street_address1',
              'street_address2',
              'county',
              'delivery_cost',
              'order_total',
              'grand_total',)

    list_display = ('full_name',
                    'order_number',
                    'date',
                    'delivery_cost',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)