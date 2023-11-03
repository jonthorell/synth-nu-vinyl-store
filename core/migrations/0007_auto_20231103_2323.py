# Generated by Django 3.2.19 on 2023-11-03 22:23

import autoslug.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20231103_2311'),
    ]

    operations = [
        migrations.CreateModel(
            name='mediatype',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('friendly_name', models.CharField(max_length=40, unique=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('slug', autoslug.fields.AutoSlugField(editable=False, populate_from='friendly_name', unique=True)),
                ('description', models.CharField(max_length=200)),
                ('updated_on', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['friendly_name'],
            },
        ),
        migrations.AlterField(
            model_name='artist',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='friendly_name', unique=True),
        ),
        migrations.AlterField(
            model_name='genre',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='friendly_name', unique=True),
        ),
    ]
