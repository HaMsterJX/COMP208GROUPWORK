from django.db import models
from django.utils import timezone

# Forum
class forum(models.Model):
    # Forum id
    forum_id = models.IntegerField(primary_key=True)
    # User id
    user = models.ForeignKey('user.user', on_delete=models.CASCADE, help_text='Please select the user')
    # The number of hits
    hits = models.IntegerField(default=0, help_text='Enter the number of hits')
    # The title of the post
    title = models.CharField(max_length=200, help_text='Enter the title of the post')
    # Comment
    comment = models.TextField(help_text='Enter the comment')
    # Tag
    tag = models.CharField(max_length=100, help_text='Enter the tag for the post')
    # Image
    img = models.ImageField(upload_to='forum_images/', blank=True, null=True, help_text='Upload an image for the post')
    # Create time
    create_time = models.DateTimeField(default=timezone.now, help_text='Enter the creation time of the post')
    # Update time
    update_time = models.DateTimeField(auto_now=True, help_text='Enter the last update time of the post')
    # Type id(Type of the post)
    type_id = models.ForeignKey('forum_classification.ForumClassification', on_delete=models.CASCADE, help_text='Select the type of the post')

    def __str__(self):
        return str(self.forum_id)


