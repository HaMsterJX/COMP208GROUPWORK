from django.db import models
from django.utils import timezone

# Singers Database
class Singer(models.Model):

    # Singer id
    singer_id = models.IntegerField(primary_key=True)
    # Singer's name
    name = models.CharField(max_length=100, help_text='Please enter the singer\'s name')
    # artist name of singer
    artist_name = models.CharField(max_length=100, help_text='Please enter the singer\'s name')
    # birthday
    birthday = models.DateField(help_text='Please enter the singer\'s birthday')
    # Birthplace of the singer
    native_place = models.CharField(max_length=100, help_text='Please enter the singer’s birthplace')
    # Photos of singers
    artist_photos = models.ImageField(upload_to='artist_photos/', blank=True, null=True, help_text='Please upload singer photo')
    # Singer's masterpiece
    represent_music = models.CharField(max_length=100, help_text='Please enter the singer\'s masterpiece')
    # Singer's Profile
    introduction_of_singer = models.TextField(help_text='Please enter the singer introduction')
    # hits
    hits = models.IntegerField(default=0, help_text='Please enter the singer clicks')
    # number of likes
    praise_len = models.IntegerField(default=0, help_text='Please enter the number of likes the singer received')
    # Recommendation index
    recommend_index = models.IntegerField(default=0, help_text='Please enter the singer recommendation index')
    # creation time
    create_time = models.DateTimeField(default=timezone.now, help_text='Please enter the creation time')
    # update time
    updatetime = models.DateTimeField(auto_now=True, help_text='Please enter the last update time')

    def __str__(self):
        return str(self.singer_id)
