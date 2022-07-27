'''
Imports relevant django packages
'''
from django.test import TestCase
from django.contrib.auth.models import User
from .models import Order


class TestCheckoutViews(TestCase):
    '''
    Checkout views Testing
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

        Order.objects.create(
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

    def test_user_details(self):
        '''
        Tests the users details
        '''

    def test_checkout_success(self):
        '''
        Tests for a successful checkout
        '''

    def test_bag_empty(self):
        '''
        Tests if the bag is empty
        '''

    def test_profile(self):
        '''
        Tests if the user has a profile
        '''