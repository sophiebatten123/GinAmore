'''
Imports relevant packages
'''
from django.http import HttpResponse


class StripeWH_Handler:
    '''
    Handles stripe webhooks
    '''
    def __init__(self, request):
        self.request = request
    
    def handle_event(self, event):
        '''
        Handles generic/unknown/unexpected webhook events
        '''
        return HttpResponse(
            content=f'Webhook has been recieved: { event["type"] }',
            status=200
        )
