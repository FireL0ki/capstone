from django.db import models

# Create your models here.

# class of Place, subclass models.Model
class Place(models.Model):
    # specify the fields which map to columns in a DB table called place
    name = models.CharField(max_length=200)
    visited = models.BooleanField(default=False)

    # string method
    def __str__(self):
        # never displayed to the user, helpful for dev to see
        return f'{self.name} visited? {self.visited}'