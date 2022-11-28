from django import forms
from .models import Place

class NewPlaceForm(forms.ModelForm):
    class Meta:
        model = Place
        # don't list the primary key field to have it auto generate
        fields = ('name', 'visited')