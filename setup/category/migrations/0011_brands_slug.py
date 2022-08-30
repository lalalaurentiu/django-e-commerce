# Generated by Django 4.1 on 2022-08-30 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0010_category_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
