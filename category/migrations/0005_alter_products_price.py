# Generated by Django 4.1 on 2022-08-17 00:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0004_brands_products'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=5),
        ),
    ]
