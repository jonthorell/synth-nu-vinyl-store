# Generated by Django 3.2.19 on 2023-11-21 00:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0012_auto_20231116_0234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='sku',
            field=models.CharField(default='change this', max_length=254),
        ),
    ]