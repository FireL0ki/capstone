from django.urls import path
from . import views

urlpatterns = [
    # any request to home page should be handled by function called place_list
    path('', views.place_list, name='place_list'),
    path('visited', views.places_visited, name='places_visited'),
    path('place/<int:place_pk>/was_visited/', views.place_was_visited, name='place_was_visited'),
    path('about', views.about, name='about'),
    path('place/<int:place_pk>/place_detail/', views.place_detail, name='place_detail'),
    path('place/<int:place_pk>/delete', views.delete_place, name='delete_place')
]