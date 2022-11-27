from django.shortcuts import render
from .models import Place

# Create your views here.

def place_list(request):
    # retrieve all the place objects
    # places = Place.objects.all()
    places = Place.objects.filter(visited=False).order_by('name')
    # render travel_wishlist/wishlist.html template, create dictionary of places
    return render(request, 'travel_wishlist/wishlist.html', {'places': places})
