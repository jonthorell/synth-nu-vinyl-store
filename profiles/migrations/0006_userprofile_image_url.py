# Generated by Django 3.2.19 on 2023-11-28 02:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0005_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='image_url',
            field=models.URLField(blank=True, max_length=1024, null=True),
        ),
    ]
