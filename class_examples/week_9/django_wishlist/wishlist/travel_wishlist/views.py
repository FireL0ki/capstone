from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm

# Create your views here.

def place_list(request):

    if request.method == 'POST':
        # create a new place form
        form = NewPlaceForm(request.POST) # creating a form from data in the request
        place = form.save() # create a model object from form -- call .save() makes a model object (place object)
        if form.is_valid(): # validate against DB constraints
            place.save() # saves place to DB
            return redirect('place_list') # reloads home page

    # retrieve all the place objects-- places = Place.objects.all()
    places = Place.objects.filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm() # used to create HTML
    # render travel_wishlist/wishlist.html template, create dictionary of places
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


def places_visited(request):
    visited = Place.objects.filter(visited=True)
    return render(request, 'travel_wishlist/visited.html', { 'visited': visited })


def place_was_visited(request, place_pk):
    if request.method == 'POST':
        # place = Place.objects.get(pk=place_pk)
        place = get_object_or_404(Place, pk=place_pk) 
        place.visited = True
        place.save()

    # return redirect('places_visited')
    return redirect('place_list')


def about(request):
    author = 'Sif'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author':author, 'about': about})