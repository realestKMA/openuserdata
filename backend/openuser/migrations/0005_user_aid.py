# Generated by Django 4.0.5 on 2022-07-10 22:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openuser', '0004_remove_user_unique_app_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='aid',
            field=models.SlugField(blank=True, help_text='App unique ID', null=True, verbose_name='App ID'),
        ),
    ]
