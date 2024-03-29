# Generated by Django 4.0.5 on 2022-08-26 20:58

from django.db import migrations, models
import openuser.models


class Migration(migrations.Migration):

    dependencies = [
        ('openuser', '0007_alter_user_gender_delete_address'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='openusercreator',
            options={},
        ),
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ['-date_joined'], 'verbose_name_plural': 'Openusers'},
        ),
        migrations.AlterField(
            model_name='openusercreator',
            name='cid',
            field=models.CharField(blank=True, help_text='The creators ID', max_length=20, null=True, verbose_name='CID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='cid',
            field=models.CharField(blank=True, help_text='The creators ID', max_length=20, null=True, verbose_name='CID'),
        ),
        migrations.AlterField(
            model_name='user',
            name='uid',
            field=models.CharField(default=openuser.models.get_random_int, help_text='User Unique ID', max_length=20, unique=True, verbose_name='UID'),
        ),
    ]
