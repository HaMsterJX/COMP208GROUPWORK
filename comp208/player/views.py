from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from .models import Player
from django.views.decorators.http import require_http_methods
import os
import random


def index(request):
    """ 展示音乐播放器 """

    return render(request, 'player/index.html')


@require_http_methods(['POST'])
def media_list(request):
    """ MP3音乐列表 """

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
    """ 加载本地的歌曲 """

    # 项目路径
    app_path = os.path.abspath(os.path.dirname(__file__))
    # 获取媒体资源目录下所有歌曲文件
    path = app_path + '/../static/media/'
    files = os.listdir(path)

    for file in files:
        print(insert_music(file))

    return HttpResponse('加载本地音乐成功！')


def insert_music(name):
    """ 把歌曲信息插入数据表 """

    # 查询歌曲是否存在
    info = Player.objects.filter(title=name).first()
    if info:
        return True

    ext = 'mp3'
    # 判断文件后缀
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

    # 随机1-10专辑封面图片
    sui_num = random.randint(1, 10)
    single.imageUrl = '/static/images/' + str(sui_num) + '.png'
    return single.save()



