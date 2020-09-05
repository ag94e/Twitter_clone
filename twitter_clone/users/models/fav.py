# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from .tweet import Tweet

class Fav(models.Model):
    """ Model for a rt in a Tweet """
    fav = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="fav_id")
    fav_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.fav.user.username
