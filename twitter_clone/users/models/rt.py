# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from .tweet import Tweet

class Rt(models.Model):
    """ Model for a rt in a Tweet """
    rt = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="rt_id")
    rt_user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.rt.user.username
