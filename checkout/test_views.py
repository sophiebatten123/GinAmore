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

    def test_checkout_url(self):
        '''
        Tests checkout URL
        '''
        response = self.client.get('/checkout')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'checkout/checkout.html')

    #def test_checkout_success_url(self):
        #'''
        #Tests for a successful checkout URL
        #'''
        #item = Order.objects.create(order_number='123456')
        #response = self.client.get(f'/checkout_success/{item.order_number}')
        #self.assertEqual(response.status_code, 200)
        #self.assertTemplateUsed(response, 'checkout/checkout_success.html')
