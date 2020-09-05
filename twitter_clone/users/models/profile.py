from django.contrib.auth.models import User
from django.db import models
from django.core.validators import RegexValidator

class Profile(models.Model):
    """ Profile model.
    A proxy model that extends the data
    with data with extra information.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone_regex = RegexValidator(
        regex = r'\+?1?\d{9,15}$',
        message = "Phone number must be entered in th format: +999999999999. Up to 15 digits allowed."
    )
    phone_number = models.CharField(
        validators=[phone_regex],
        max_length=15,
        blank=True
    )
    picture = models.ImageField(
        upload_to='users/pictures',
        blank=True,
        null=True
    )
    followers = models.IntegerField(default=0)
    following = models.IntegerField(default=0)
    totalTweets = models.IntegerField(default=0)
    about_me = models.TextField(max_length=250, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        """Return username."""
        return self.user.username