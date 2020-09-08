""" Users and tweets views """
# Django
from django.shortcuts import render

# Utilities
from datetime import datetime
import time
tweets = [
    {
        'user':{
            'name':'Juan Alberto',
            'username': '@juanAlberto',
            'picture': 'https://i.picsum.photos/id/490/200/200.jpg?hmac=7WZhaN9NS8sb08YmpHre_3NGnVUsmH8X5W_GlG2Mry4'  
            },
        'tweet': 'I like pizza',
        'images': {
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'image4': 'null'
        },
        "time" : datetime.now(),
        "fav": 12,
        "rt": 4,
        "replies": 2
    },
    {
        'user':{
            'name':'Juan Alberto',
            'username': '@juanAlberto',
            'picture': 'https://i.picsum.photos/id/490/200/200.jpg?hmac=7WZhaN9NS8sb08YmpHre_3NGnVUsmH8X5W_GlG2Mry4'  
            },
        'tweet': 'I like pizza',
        'images': {
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'image4': 'null'
        },
        "time" : datetime.now(),
        "fav": 12,
        "rt": 4,
        "replies": 2
    },
    {
        'user':{
            'name':'Juan Alberto',
            'username': '@juanAlberto',
            'picture': 'https://i.picsum.photos/id/490/200/200.jpg?hmac=7WZhaN9NS8sb08YmpHre_3NGnVUsmH8X5W_GlG2Mry4'  
            },
        'tweet': 'I like pizza',
        'images': {
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'image4': 'null'
        },
        "time" : datetime.now(),
        "fav": 12,
        "rt": 4,
        "replies": 2
    },
    {
        'user':{
            'name':'Juan Alberto',
            'username': '@juanAlberto',
            'picture': 'https://i.picsum.photos/id/490/200/200.jpg?hmac=7WZhaN9NS8sb08YmpHre_3NGnVUsmH8X5W_GlG2Mry4'  
            },
        'tweet': 'I like pizza',
        'images': {
            'image1': 'null',
            'image2': 'null',
            'image3': 'null',
            'image4': 'null'
        },
        "time" : datetime.now(),
        "fav": 12,
        "rt": 4,
        "replies": 2
    },
]

def list_tweets(request):
    """ list tweets """
    return render(request, 'feed.html', {'tweets': tweets})