'''
Imports relevant django packages
'''
from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .views import profile


class TestProfileViews(TestCase):
    '''
    Profile views Testing
    '''
    def setUp(self):
        '''
        Sets up the test profile data
        '''
        self.profile_url = reverse('profile')
        
        self.client = Client()
        self.user = User.objects.create_user(
            'test',
            'test@test.com',
            'testpassword')

    def test_profile_url(self):
        '''
        Tests the user profile is generated when logged in
        '''
        self.client.login(username='test', password='testpassword')
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'profiles/profile.html')
