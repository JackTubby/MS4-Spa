from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Treatment, Category


def all_treatments(request):
    """ A view to return all treatments, including sorting and search quries """

    treatments = Treatment.objects.all()
    query = None
    categories = None
    sort = None
    direction = None

    if request.GET:
        if 'sort' in request.GET:
            sortkey = request.GET['sort']
            sort = sortkey
            if sortkey == 'name':
                sortkey = 'lower_name'
                treatments = treatments.annotate(lower_name=Lower('name'))
            if sortkey == 'category':
                sortkey = 'category__name'
            if 'direction' in request.GET:
                direction = request.GET['direction']
                if direction == 'desc':
                    sortkey = f'-{sortkey}'
            treatments = treatments.order_by(sortkey)

        if 'category' in request.GET:
            categories = request.GET['category'].split(',')
            treatments = treatments.filter(category__name__in=categories)
            categories = Category.objects.filter(name__in=categories)

        if 'q' in request.GET:
            query = request.GET['q']
            if not query:
                messages.error(request, "You didn't enter any search criteria!")
                return redirect(reverse('treatments'))
    
            queries = Q(name__icontains=query) | Q(description__icontains=query)
            treatments = treatments.filter(queries)
 
    current_sorting = f'{sort}_{direction}'

    context = {
        'treatments': treatments,
        'search_term': query,
        'current_categories': categories,
        'current_sorting': current_sorting,
    }

    return render(request, 'treatments/treatments.html', context)


def treatment_detail(request, treatment_id):
    """ A view to show individual treatment details """

    treatment = get_object_or_404(Treatment, pk=treatment_id)

    context = {
        'treatment': treatment,
    }

    return render(request, 'treatments/treatment_detail.html', context)
