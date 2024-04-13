from django.db import models
from django.utils import timezone

# user database
class user(models.Model):
    # User id
    user_id = models.IntegerField(primary_key=True)
    # Gender
    gender = models.CharField(max_length=100, help_text='Please enter the gender')
    # Age
    age = models.IntegerField(default=0, help_text='Please enter the age')
    # Login state
    login_state = models.CharField(max_length=100, help_text='Please enter the user state')
    # Phone
    phone = models.CharField(max_length=100, help_text='Please enter the phone number')
    # Username
    username = models.CharField(max_length=100, help_text='Please enter the username')
    # Nickname
    nickname = models.CharField(max_length=100, help_text='Please enter the nickname')
    # Password
    password = models.CharField(max_length=100, help_text='Please enter the password')
    # Email
    email = models.EmailField(help_text='Please enter the email')
    # Avatar
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True, help_text='Please upload the avatar')
    # Birthday
    birthday = models.DateField(help_text='Please enter the user\'s birthday')
    # Create time
    create_time = models.DateTimeField(default=timezone.now, help_text='Please enter the account creation time')
    # Examine state
    examine_state = models.IntegerField(default=0, help_text='Please enter if it has been registered')

    def __str__(self):
        return self.username
