# Generated by Django 4.1 on 2022-08-16 19:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_category_svg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='svg',
            field=models.TextField(blank=True, null=True),
        ),
    ]
