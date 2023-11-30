# Generated by Django 3.2.19 on 2023-11-30 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0015_remove_userprofile_default_currency'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='currency',
            field=models.IntegerField(blank=True, choices=[(0, 'USD'), (1, 'SEK')], default=0, null=True),
        ),
    ]
