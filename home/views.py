from django.shortcuts import render


# Home Index Page
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')


# Faq Page
def faq(request):
    """ A view to return the faq page """

    return render(request, 'home/faq.html')
