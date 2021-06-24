from django.shortcuts import render


# Home Index Page
def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
