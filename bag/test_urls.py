from django.test import SimpleTestCase
from django.urls import reverse, resolve
from bag.views import view_bag


class TestBagUrls(SimpleTestCase):
    '''
    Testing of the bag URLS
    '''
    def test_view_bag(self):
        '''
        Tests the view bag URL
        '''
        url = reverse('view_bag')
        self.assertEqual(resolve(url).func, view_bag)
