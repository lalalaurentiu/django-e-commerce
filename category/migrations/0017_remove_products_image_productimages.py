# Generated by Django 4.1 on 2022-09-02 23:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0016_remove_products_raiting_productraiting'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='products',
            name='image',
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/Products')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='productImages', to='category.products')),
            ],
        ),
    ]
