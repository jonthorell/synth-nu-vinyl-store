# Generated by Django 3.2.19 on 2023-12-03 00:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0016_rename_prod_testimonial_testimonial_reviewed'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonial',
            old_name='reviewed',
            new_name='article',
        ),
    ]
