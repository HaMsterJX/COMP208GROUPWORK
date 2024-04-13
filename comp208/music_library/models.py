from django.db import models
from django.utils import timezone

class MusicLibrary(models.Model):
    # 歌曲id
    music_id = models.IntegerField(primary_key=True)
    # 歌曲名称
    song_name = models.CharField(max_length=100, help_text='Please enter the song name')
    # 音乐类别
    music_category = models.CharField(max_length=100, help_text='Please enter the music category')
    # 歌手姓名
    singer_name = models.CharField(max_length=100, help_text='Please enter the singer name')
    # 歌手id——外键
    singer_id = models.ForeignKey('Singer.Singer', on_delete=models.CASCADE, help_text='Please enter the singer ID')
    # 发行日期
    issue_date = models.DateField(help_text='Please enter the issue date of the song')
    # 音频频率
    audio_frequency = models.CharField(max_length=100, help_text='Please enter the audio frequency')
    # 封面图片
    cover = models.ImageField(upload_to='song_covers/', blank=True, null=True, help_text='Please upload the cover image')
    # 视频文件
    video = models.FileField(upload_to='song_videos/', blank=True, null=True, help_text='Please upload the video file')
    # 歌词
    lyric = models.TextField(help_text='Please enter the lyrics')
    # 歌曲介绍
    intro = models.TextField(help_text='Please enter the song introduction')
    # 点击量
    hits = models.IntegerField(default=0, help_text='Please enter the number of hits')
    # 获赞数
    praise_len = models.IntegerField(default=0, help_text='Please enter the number of likes')
    # 推荐指数
    recommend = models.IntegerField(default=0, help_text='Please enter the recommendation index')
    # 创建时间
    create_time = models.DateTimeField(default=timezone.now, help_text='Please enter the creation time')
    # 更新时间
    update_time = models.DateTimeField(auto_now=True, help_text='Please enter the last update time')

    def __str__(self):
        return self.song_name
