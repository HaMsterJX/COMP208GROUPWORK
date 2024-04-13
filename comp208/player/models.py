from django.db import models
from music_library.models import MusicLibrary

class Player(models.Model):
    # Assuming there's at least one MusicLibrary entry and using its ID as the default
    song = models.ForeignKey(MusicLibrary, on_delete=models.CASCADE, null=True, help_text='Select the song to play')
    singer_url = models.URLField(max_length=200, blank=True, help_text='Enter the URL to the singer\'s profile')
    singer_image_url = models.URLField(max_length=200, blank=True, help_text='Enter the URL to the singer\'s image')

    def __str__(self):
        return f"{self.song.song_name} by {self.song.singer_name}"
