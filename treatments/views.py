from django.shortcuts import render
from .models import Treatment


from django.shortcuts import render


def all_treatments(request):
    """ A view to return all treatments, including sorting and search quries """

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)

