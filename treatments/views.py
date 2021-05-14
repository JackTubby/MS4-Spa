from django.shortcuts import get_object_or_404, redirect, reverse, render
from django.contrib import messages
from django.db.models import Q
from .models import Treatment, Category


from django.shortcuts import render


def all_treatments(request):
    """ A view to return all treatments, including sorting and search quries """

    treatments = Treatment.objects.all()
    query = None
    categories = None


    if request.GET:
        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treatments = treatments.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
            
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            treatments = treatments.filter(queries)

    context = {
        'treatments': treatments,
        'search_term': query,
        'current_categories': categories,
    }

    return render(request, 'treatments/treatments.html', context)


def treatment_detail(request, treatment_id):
    """ A view to show individual treatment details """

    treatments = get_object_or_404(Treatment, pk=treatment_id)

    context = {
        'treatments': treatments,
    }

    return render(request, 'treatments/treatment_detail.html', context)
