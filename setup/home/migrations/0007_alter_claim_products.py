# Generated by Django 4.1 on 2022-09-21 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0019_productraiting_message'),
        ('home', '0006_claim_deal_choices_claim_deal_sum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='claim',
            name='products',
            field=models.ManyToManyField(related_name='deals', to='category.products'),
        ),
    ]
