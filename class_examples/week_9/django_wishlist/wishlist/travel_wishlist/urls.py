from django.urls import path
from . import views

urlpatterns = [
    # any request to home page should be handled by function called place_list
    path('', views.place_list, name='place_list'),

]