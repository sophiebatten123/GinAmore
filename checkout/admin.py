from django.contrib import admin
from .models import Order, OrderLineItem


class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('lineitem_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)
    readonly_fields = ('order_number',
                       'delivery_cost',
                       'order_total',
                       'grand_total',
                       'date',
                       'original_bag',
                       'stripe_pid',
                       )
                       
    fields = ('full_name',
              'order_number',
              'user_profile',
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
              'grand_total',
              'original_bag',
              'stripe_pid',)

    list_display = ('full_name',
                    'order_number',
                    'date',
                    'delivery_cost',
                    'order_total',
                    'grand_total',)

    ordering = ('-date',)

admin.site.register(Order, OrderAdmin)