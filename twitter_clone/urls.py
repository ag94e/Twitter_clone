from django.contrib import admin
from django.urls import path

from twitter_clone.users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', users_views.list_tweets)
]
