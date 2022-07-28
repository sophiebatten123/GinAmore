'''
Imports relevant django packages
'''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order


class TestCheckoutModels(TestCase):
    '''
    Checkout models Testing
    '''
    def test_checkout(self):
        '''
        Sets up the test checkout data
        '''
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com'
        )
        test_user.save()

    def test_order_number(self):
        '''
        Tests that the correct order number is produced
        '''
        order = Order.objects.create(
            order_number='123456',
            full_name='Test User',
            phone_number='1234567890',
            email='test@test.com',
            country='Test Country',
            town_or_city='Test City',
            postcode='Test Postcode',
            street_address1='Test Address',
            county='Test County'
            )
        self.assertTrue(isinstance(order, Order))
        self.assertEqual(str(order), '123456')
