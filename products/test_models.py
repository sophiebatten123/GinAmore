'''
Imports relevant django packages
'''
from django.test import TestCase
from django.contrib.auth.models import User
from products.models import Product


class TestProductsModels(TestCase):
    '''
    Products models Testing
    '''
    def test_checkout(self):
        '''
        Sets up the test product data
        '''
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com'
        )
        test_user.save()

    def test_product_name(self):
        '''
        Tests that the product name is produced
        '''
        product = Product.objects.create(
            name='test',
            description='test description',
            price='99.99',
            rating='9.9',
            image='test'
            )
        self.assertTrue(isinstance(product, Product))
        self.assertEqual(str(product), 'test')
