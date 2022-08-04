from django.shortcuts import render


def cocktails(request):
    '''
    A view to return the render of the cocktails template
    '''
    return render(request, 'cocktails/cocktails.html')
