from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class of Place, subclass models.Model
class Place(models.Model):
    # specify the fields which map to columns in a DB table called place
    user = models.ForeignKey('auth.User', null=False, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)
    notes = models.TextField(blank=True, null=True)
    date_visited = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='user_images/', blank=True, null=True)

    # string method
    def __str__(self):
        # never displayed to the user, helpful for dev to see
        # return f'{self.name} visited? {self.visited}'

        # check if there is a photo url
        photo_str = self.photo.url if self.photo else 'no photo'
        notes_str = self.notes[100:] if self.notes else 'no notes' # truncated to the first 100 characters
        return f'{self.name}, visited? {self.visited} on {self.date_visited}. Notes: {notes_str}. Photo: {photo_str}'