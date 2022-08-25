'''
Imports relevant django packages
'''
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Order
from .views import checkout, checkout_success


class TestCheckoutViews(TestCase):
    '''
    Checkout views Testing
    '''
    def setUp(self):
        '''
        Sets up the test checkout data
        '''
        self.client = Client()
        self.user = User.objects.create_user(
            'test',
            'test@test.com',
            'testpassword')

    def test_checkout_url_empty_bag(self):
        '''
        Tests checkout URL for logged in users with no bag items
        '''
        self.client.login(username='test', password='testpassword')
        response = self.client.get(reverse('products'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')
