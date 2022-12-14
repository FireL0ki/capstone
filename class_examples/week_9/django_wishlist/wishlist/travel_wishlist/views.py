from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages
from .forms import TripReviewForm

# Create your views here.

@login_required
def place_list(request):

    if request.method == 'POST':
        # create a new place form
        form = NewPlaceForm(request.POST) # creating a form from data in the request
        place = form.save(commit=False) # create new Place (a model object) from form -- call .save() makes a model object (place object)
        place.user = request.user
        if form.is_valid(): # validate against DB constraints
            place.save() # saves place to DB
            return redirect('place_list') # reloads home page

    # retrieve all the place objects-- places = Place.objects.all()
    places = Place.objects.filter(user=request.user).filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # used to create HTML
    # render travel_wishlist/wishlist.html template, create dictionary of places
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


@login_required
def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


@login_required
def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.visited = True
            place.save()
        else:
            return HttpResponseForbidden()

    # return redirect('places_visited')
    return redirect('place_list')


@login_required
def place_details(request, place_pk):
    place = get_object_or_404(Place, pk=place_pk)

    # does this place belong to the current user?
    if place.user != request.user:
        return HttpResponseForbidden()
    # is this a GET (show data + form) or POST (update place object) request?

    # if POST request, validate form data and update.
    if request.method == 'POST':
        # request info from the user and use it to update the place instance
        form = TripReviewForm(request.POST, request.FILES, instance=place)
        if form.is_valid(): # are all required fields filled in with correct data type
            form.save()
            messages.info(request, 'Trip information updated.')
        else:
            messages.error(request, form.errors) # temporary- refine later

        return redirect('place_details', place_pk=place_pk)

    else:
        # if GET request, show Place infor and form
        # if place is visited, show form; if place is not visited, no form
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/place_details.html', {place: place, 'review_form': review_form})
        else:
            return render(request, 'travel_wishlist/place_details.html', {place: place})

    # return render(request, 'travel_wishlist/place_details.html', {'place': place})

@login_required
def delete_place(request, place_pk):
    place = get_object_or_404(Place, place_pk)
    # ensure the correct user is deleting their own places
    if place.user == request.user:
        place.delete()
        return redirect('place_list')
    else:
        return HttpResponseForbidden()


def about(request):
    author = 'Sif'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about': about})