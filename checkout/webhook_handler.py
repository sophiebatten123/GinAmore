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
            content=f'Unhandled webhook has been recieved: { event["type"] }',
            status=200
        )

    def handle_payment_intent_succeeded(self, event):
        '''
        Handles the payment_intent.succeeded webhook from Stripe
        '''
        return HttpResponse(
            content=f'Webhook has been recieved: { event["type"] }',
            status=200
        )

    def handle_payment_intent_payment_failed(self, event):
        '''
        Handles the payment_intent.payment_failed webhook from Stripe
        '''
        return HttpResponse(
            content=f'Webhook has been recieved: { event["type"] }',
            status=200
        )
