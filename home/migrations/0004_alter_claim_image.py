# Generated by Django 4.1 on 2022-08-16 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_claim_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='image',
            field=models.ImageField(upload_to='images/Claim'),
        ),
    ]