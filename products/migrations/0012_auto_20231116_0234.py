# Generated by Django 3.2.19 on 2023-11-16 01:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0011_alter_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='price_currency',
            field=models.CharField(default='USD', max_length=3),
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]