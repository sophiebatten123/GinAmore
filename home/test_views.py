'''
Imports relevant django packages
'''
from django.test import TestCase, Client


class TestHomeViews(TestCase):
    '''
    Products views Testing
    '''
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        '''
        Tests home view URL
        '''
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'home/index.html')
