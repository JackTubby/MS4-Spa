from django.shortcuts import get_object_or_404, render
from .models import Treatment


from django.shortcuts import render


def all_treatments(request):
    """ A view to return all treatments, including sorting and search quries """

    treatments = Treatment.objects.all()

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatments.html', context)


def treatment_detail(request, treatment_id):
    """ A view to show individual treatment details """

    treatments = get_object_or_404(Treatment, pk=treatment_id)

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatment_detail.html', context)
