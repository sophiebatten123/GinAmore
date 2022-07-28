'''
Imports relevant django packages
'''
from django.test import TestCase, Client


class TestBagViews(TestCase):
    '''
    Bag views Testing
    '''
    def setUp(self):
        '''
        Sets up the testing enviroment
        '''
        self.client = Client()

    def test_bag_view(self):
        '''
        Tests bag view URL
        '''
        response = self.client.get('/bag/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
