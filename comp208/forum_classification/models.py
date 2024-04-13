from django.db import models
from django.utils import timezone

#  Forum category
class ForumClassification(models.Model):
    # Forum id
    type_id = models.AutoField(primary_key=True)
    # The name of the forum type
    name = models.CharField(max_length=100, help_text='Enter the name of the forum type')
    # The description of the forum type
    description = models.TextField(help_text='Enter a description of the forum type')
    # The icon for the forum type
    icon = models.ImageField(upload_to='forum_type_icons/', blank=True, null=True, help_text='Upload an icon for the forum type')
    # Create time
    create_time = models.DateTimeField(default=timezone.now, help_text='Enter the creation time of the forum type')
    # Update time
    update_time = models.DateTimeField(auto_now=True, help_text='Enter the last update time of the forum type')

    def __str__(self):
        return str(self.type_id)
