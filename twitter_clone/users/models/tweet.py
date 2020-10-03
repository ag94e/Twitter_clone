# Django
from django.db import models
from django.contrib.auth.models import User

class Tweet(models.Model):
    """ Tweet model.
    A model of tweets that user can make.
    """
    text_body = models.CharField(max_length=140, null=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rt = models.IntegerField(null=False, default=0)
    fav = models.IntegerField(null=False, default=0)
    replies = models.IntegerField(null=True, default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username