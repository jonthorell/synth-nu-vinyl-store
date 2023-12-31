# Generated by Django 3.2.19 on 2023-11-30 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0009_auto_20231130_1020'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='default_currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='newsletter',
            field=models.IntegerField(choices=[(0, 'No'), (1, 'Yes')], default=0),
        ),
    ]
