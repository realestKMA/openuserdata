# Generated by Django 4.0.4 on 2022-08-29 14:27

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openuser', '0008_alter_openusercreator_options_alter_user_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='openusercreator',
            name='cid',
            field=models.CharField(blank=True, help_text='Openuser Creator Unique ID', max_length=20, null=True, verbose_name='CID'),
        ),
        migrations.AlterField(
            model_name='openusercreator',
            name='id',
            field=models.BigAutoField(editable=False, help_text='Openuser Creator Database ID', primary_key=True, serialize=False, unique=True, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='openusercreator',
            name='username',
            field=models.CharField(blank=True, help_text='Openuser Creator username', max_length=255, null=True, verbose_name='Username'),
        ),
        migrations.AlterField(
            model_name='user',
            name='app_name',
            field=models.CharField(help_text='The name of this Openuser data. Spaces are replaced with hyphens', max_length=20, validators=[django.core.validators.RegexValidator(message='Must begin and end with a letter. And can only contain letters, numbers and hyphens', regex='^[a-zA-Z]([\\w -]*[a-zA-Z])?$'), django.core.validators.MinLengthValidator(limit_value=4)], verbose_name='App Name'),
        ),
    ]
