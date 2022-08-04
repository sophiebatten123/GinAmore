from django.shortcuts import render


def ourstory(request):
    '''
    A view to return the render of the our story template
    '''
    return render(request, 'ourstory/ourstory.html')
