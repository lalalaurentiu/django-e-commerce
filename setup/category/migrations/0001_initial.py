# Generated by Django 4.1 on 2022-08-16 18:19

from django.db import migrations, models
import fontawesome_5.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(max_length=100)),
                ('image', fontawesome_5.fields.IconField(blank=True, max_length=60)),
            ],
        ),
    ]
