from django.db import models
from django.utils import timezone

class MusicLibrary(models.Model):
    # Music id
    music_id = models.IntegerField(primary_key=True)
    # Music name
    song_name = models.CharField(max_length=100, help_text='Please enter the song name')
    # Music category
    music_category = models.CharField(max_length=100, help_text='Please enter the music category')
    # Singer name
    singer_name = models.CharField(max_length=100, help_text='Please enter the singer name')
    # singer id - foreign key
    singer_id = models.ForeignKey('Singer.Singer', on_delete=models.CASCADE, help_text='Please enter the singer ID')
    # Issue date of the song
    issue_date = models.DateField(help_text='Please enter the issue date of the song')
    # Audio frequency
    audio_frequency = models.CharField(max_length=100, help_text='Please enter the audio frequency')
    # Cover image
    cover = models.ImageField(upload_to='song_covers/', blank=True, null=True, help_text='Please upload the cover image')
    # Video file
    video = models.FileField(upload_to='song_videos/', blank=True, null=True, help_text='Please upload the video file')
    # Lyric of the song
    lyric = models.TextField(help_text='Please enter the lyrics')
    # Song introduction
    intro = models.TextField(help_text='Please enter the song introduction')
    # Hits
    hits = models.IntegerField(default=0, help_text='Please enter the number of hits')
    # The number of likes
    praise_len = models.IntegerField(default=0, help_text='Please enter the number of likes')
    # Recommendation index
    recommend = models.IntegerField(default=0, help_text='Please enter the recommendation index')
    # Create time
    create_time = models.DateTimeField(default=timezone.now, help_text='Please enter the creation time')
    # Update time
    update_time = models.DateTimeField(auto_now=True, help_text='Please enter the last update time')

    def __str__(self):
        return self.song_name
