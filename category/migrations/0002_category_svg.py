# Generated by Django 4.1 on 2022-08-16 18:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='svg',
            field=models.TextField(null=True),
        ),
    ]
