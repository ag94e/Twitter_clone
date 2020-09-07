""" Users and tweets views """
# Django
from django.shortcuts import render

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
        }
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
        }
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
        }
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
        }
    },
]

def list_tweets(request):
    """ list tweets """
    return render(request, 'feed.html', {'tweets': tweets})