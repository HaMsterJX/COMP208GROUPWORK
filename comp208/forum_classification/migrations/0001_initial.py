# Generated by Django 4.1 on 2024-03-24 17:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Forum_Classification',
            fields=[
                ('type_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(help_text='Enter the name of the forum type', max_length=100)),
                ('description', models.TextField(help_text='Enter a description of the forum type')),
                ('icon', models.ImageField(blank=True, help_text='Upload an icon for the forum type', null=True, upload_to='forum_type_icons/')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now, help_text='Enter the creation time of the forum type')),
                ('update_time', models.DateTimeField(auto_now=True, help_text='Enter the last update time of the forum type')),
            ],
        ),
    ]
