# Generated by Django 4.0.5 on 2022-07-11 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openuser', '0005_user_aid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='aid',
            field=models.SlugField(blank=True, help_text='App unique ID', max_length=255, null=True, verbose_name='App ID'),
        ),
    ]
