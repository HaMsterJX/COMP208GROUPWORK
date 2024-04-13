# Generated by Django 4.1 on 2024-03-24 18:28

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0002_alter_user_user_id'),
        ('forum_classification', '0002_rename_forum_classification_forumclassification'),
    ]

    operations = [
        migrations.CreateModel(
            name='forum',
            fields=[
                ('forum_id', models.IntegerField(primary_key=True, serialize=False)),
                ('hits', models.IntegerField(default=0, help_text='Enter the number of hits')),
                ('title', models.CharField(help_text='Enter the title of the post', max_length=200)),
                ('comment', models.TextField(help_text='Enter the comment')),
                ('tag', models.CharField(help_text='Enter the tag for the post', max_length=100)),
                ('img', models.ImageField(blank=True, help_text='Upload an image for the post', null=True, upload_to='forum_images/')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='Enter the creation time of the post')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='Enter the last update time of the post')),
                ('type_id', models.ForeignKey(help_text='Select the type of the post', on_delete=django.db.models.deletion.CASCADE, to='forum_classification.forumclassification')),
                ('user', models.ForeignKey(help_text='Please select the user', on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
