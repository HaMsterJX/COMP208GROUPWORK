# Generated by Django 4.1 on 2024-04-11 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musiclibrary',
            name='music_id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
