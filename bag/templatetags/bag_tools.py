'''
Imports relevant django packages
'''
from django import template

register = template.Library()


@register.filter(name='calc_subtotal')
def calc_subtotal(price, quantity):
    '''
    Calculates the bags subtotal
    '''
    return price * quantity
