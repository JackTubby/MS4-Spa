from django.shortcuts import render


# Home Index Page
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Terms of service Page
def tos(request):
    """ A view to return the tos page """

    return render(request, 'home/tos.html')


# Terms of service Page
def faq(request):
    """ A view to return the faq page"""

    return render(request, 'home/faq.html')
