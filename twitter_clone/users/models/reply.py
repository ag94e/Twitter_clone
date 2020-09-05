# Django
from django.db import models
from django.contrib.auth.models import User

# Models
from .tweet import Tweet

class Reply(models.Model):
    """ Model for a rt in a Tweet """
    reply = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="reply")
    reply_user = models.ForeignKey(User, on_delete=models.CASCADE)
    reply_tweet = models.ForeignKey(Tweet, on_delete=models.CASCADE, related_name="reply_tweet")

    def __str__(self):
        return self.fav.user.username
