# Generated by Django 4.1 on 2022-09-06 09:11

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_order_address2_order_region'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(default="123", max_length=128, region=None),
            preserve_default=False,
        ),
    ]
