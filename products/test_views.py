'''
Imports relevant django packages
'''
from django.test import TestCase, Client
from django.urls import reverse
from .models import Product


class TestBagViews(TestCase):
    '''
    Products views Testing
    '''
    def setUp(self):
        '''
        Sets up the testing enviroment
        '''
        self.client = Client()
        self.product_url = reverse('products')
        self.product_detail_url = reverse('product_detail', args=[1])
        
        self.product_example = Product.objects.create(
            name='test',
            description='test description',
            price='99.99',
            rating='9.9',
            image='test'
        )

    def test_view_all_products(self):
        '''
        Tests all products URL
        '''
        response = self.client.get(self.product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/products.html')

    def test_product_detail_url(self):
        '''
        Tests product detail URL
        '''
        response = self.client.get(self.product_detail_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'products/product_detail.html')
