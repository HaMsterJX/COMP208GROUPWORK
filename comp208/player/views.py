from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player
from django.views.decorators.http import require_http_methods
import os
import random


def index(request):
    """ Demonstrate the music player """

    return render(request, 'player/index.html')


@require_http_methods(['POST'])
def media_list(request):
    """ MP3 Music Lists """

    mediaList = Player.objects.all()

    arr = []
    for item in mediaList:
        arr.append({
            'id': item.id,
            'title': item.title,
            'singer': item.singer,
            'songUrl': item.songUrl,
            'imageUrl': item.imageUrl,
        })

    return JsonResponse({'list': arr})


def load_music(request):
    """ Loading Local Songs """

    #  Project Paths
    app_path = os.path.abspath(os.path.dirname(__file__))
    # Get all song files in the Media Resources directory
    path = app_path + '/../static/media/'
    files = os.listdir(path)

    for file in files:
        print(insert_music(file))

    return HttpResponse(' Loading Local Music Successfully！')


def insert_music(name):
    """ Insert song information into the data table """

    #  Check if the song exists
    info = Player.objects.filter(title=name).first()
    if info:
        return True

    ext = 'mp3'
    #  Determine file suffix
    fileInfo = name.split('.')
    if len(fileInfo) != 2:
        return False

    if fileInfo[1] != ext:
        return False

    single = Player()
    single.title = name
    signers = name.split('-')
    single_1 = signers[1].strip('') if len(signers) > 1 else ''
    single.singer = single_1.strip('.mp3')
    single.songUrl = '/static/media/' + name

    # Random 1-10 album cover images
    sui_num = random.randint(1, 10)
    single.imageUrl = '/static/images/' + str(sui_num) + '.png'
    return single.save()



