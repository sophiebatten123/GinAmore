'''
Imports relevant django packages
'''
from django.test import TestCase
from django.contrib.auth.models import User


class TestBagViews(TestCase):
    '''
    Bag views Testing
    '''
    def test_bag(self):
        '''
        Sets up the test bag views
        '''
        test_user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@test.com'
        )
        test_user.save()

    def test_view_bag_url(self):
        '''
        Tests view bag URL
        '''
        response = self.client.get('/bag')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bag/bag.html')
