# Generated by Django 3.2.19 on 2023-11-14 00:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_contact_message_complete'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='contact_message',
            options={'ordering': ['-created_on']},
        ),
    ]
