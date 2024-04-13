# Generated by Django 4.1 on 2024-04-12 14:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0002_alter_musiclibrary_music_id'),
        ('player', '0002_rename_song_player'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='player',
            name='imageUrl',
        ),
        migrations.RemoveField(
            model_name='player',
            name='singer',
        ),
        migrations.RemoveField(
            model_name='player',
            name='songUrl',
        ),
        migrations.RemoveField(
            model_name='player',
            name='title',
        ),
        migrations.AddField(
            model_name='player',
            name='singer_image_url',
            field=models.URLField(blank=True, help_text="Enter the URL to the singer's image"),
        ),
        migrations.AddField(
            model_name='player',
            name='singer_url',
            field=models.URLField(blank=True, help_text="Enter the URL to the singer's profile"),
        ),
        migrations.AddField(
            model_name='player',
            name='song',
            field=models.ForeignKey(help_text='Select the song to play', null=True, on_delete=django.db.models.deletion.CASCADE, to='music_library.musiclibrary'),
        ),
    ]