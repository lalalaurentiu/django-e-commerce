# Generated by Django 4.1 on 2022-08-17 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0005_alter_products_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='products',
            name='discount',
            field=models.FloatField(default=0),
        ),
    ]