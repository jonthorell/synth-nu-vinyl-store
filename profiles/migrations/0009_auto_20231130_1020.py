# Generated by Django 3.2.19 on 2023-11-30 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0008_alter_userprofile_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='newsletter',
            field=models.IntegerField(choices=[(0, 'New'), (1, 'Second hand')], default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]
