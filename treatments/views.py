from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Avg
from django.db.models import Q
from django.db.models.functions import Lower

from .models import Treatment, Category, Rating
from profiles.models import UserProfile
from checkout.models import Order
from .forms import TreatmentForm, RatingForm


def all_treatments(request):
    """ A view to return all treatments, including sorting and search queries """

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
    # Get treatment
    treatment = get_object_or_404(Treatment, pk=treatment_id)
    current_rating_obj = []
    current_rating = []
    # get all ratings
    rating_obj = Rating.objects.all()
    # Filter rating (work out average)
    current_rating_obj = Rating.objects.filter(
        treatment_id=treatment_id).aggregate(Avg('rate'))
    # Current rating average
    current_rating = current_rating_obj['rate__avg']
    # Rating count
    rating_count = rating_obj.filter(treatment_id=treatment_id).count()

    # Get users order history if treatment is in history they can add a rating
    user_purchased = False
    profile = None
    profile_orders = None
    # Check user is logged in
    if request.user.is_authenticated:
        # Get specific user
        profile = get_object_or_404(UserProfile, user=request.user)
        # Get all orders from user profile
        profile_orders = profile.orders.all()
        # check order is in current users profile
        for order in profile_orders:
            all_lineitems = order.lineitems.all()
            for item in all_lineitems:
                if item.treatment == treatment:
                    user_purchased = True
                else:
                    return redirect(reverse('treatment_detail', args=[treatment.id]))
    else:
        messages.error(request, 'Only authenticated users can do that!')
        return redirect(reverse('treatment_detail', args=[treatment.id]))
    context = {
        'treatment': treatment,
        'rating_obj': rating_obj,
        'rating_count': rating_count,
        'current_rating': current_rating,
        'user_purchased': user_purchased,
    }

    return render(request, 'treatments/treatment_detail.html', context)


@login_required
def add_treatment(request):
    """ Add a treatment to the store """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES)
        if form.is_valid():
            treatment = form.save()
            messages.success(request, 'Successfully added a treatment.')
            return redirect(reverse('treatment_detail', args=[treatment.id]))
        else:
            messages.error(request, 'Failed to add a treatment. Please make sure the form is valid!')
    else:
        form = TreatmentForm()
    template = 'treatments/add_treatment.html'
    context = {
        'form': form,
    }
    return render(request, template, context)


@login_required
def edit_treatment(request, treatment_id):
    """ Edit a treatment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    treatment = get_object_or_404(Treatment, pk=treatment_id)
    if request.method == 'POST':
        form = TreatmentForm(request.POST, request.FILES, instance=treatment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Successfully updated treatment.')
            return redirect(reverse('treatment_detail', args=[treatment.id]))
        else:
            messages.error(request, 'Failed to update treatment. Please make sure the form is valid!')
    else:
        form = TreatmentForm(instance=treatment)
        messages.info(request, f'You are editing {treatment.name}')

    template = 'treatments/edit_treatment.html'
    context = {
        'form': form,
        'treatment': treatment,
    }
    return render(request, template, context)


@login_required
def delete_treatment(request, treatment_id):
    """ Delete a treatment """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry only store owners can do that')
        return redirect(reverse('home'))

    treatment = get_object_or_404(Treatment, pk=treatment_id)
    treatment.delete()
    messages.success(request, 'Treatment deleted.')
    return redirect(reverse('treatments'))


@login_required
def add_rating(request, treatment_id):
    """ Add a rating to a treatment"""
    profile = None
    profile_orders = None
    profile = get_object_or_404(UserProfile, user=request.user)
    treatment = get_object_or_404(Treatment, pk=treatment_id)
    user_purchased = False
    profile_orders = profile.orders.all()
    for order in profile_orders:
        all_lineitems = order.lineitems.all()
        for item in all_lineitems:
            if item.treatment == treatment:
                user_purchased = True
    if user_purchased == True:
        if request.method == 'POST':
            form = RatingForm(request.POST, request.FILES)
            if form.is_valid():
                rating = form.save(commit=False)
                rating.user = request.user
                rating.treatment = get_object_or_404(Treatment, pk=treatment_id)
                rating = form.save()
                messages.success(request, 'Successfully added a rating.')
                return redirect(reverse('treatment_detail', args=[treatment.id]))
            else:
                messages.error(request, 'Failed to add a rating. Please make sure the form is valid!')
        else:
            form = RatingForm()
    else:
        messages.error(request, 'Only users who purchased this treatment can set ratings!')
        return redirect(reverse('treatment_detail', args=[treatment.id]))
    template = 'treatments/add_rating.html'
    context = {
        'treatment': treatment,
        'user_purchased': user_purchased,
        'form': form,
    }
    return render(request, template, context)


def refund_policy(request):
    """ A view to return the refund policy """

    return render(request, 'treatments/refund-policy.html')
