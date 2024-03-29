# Generated by Django 4.0.6 on 2022-08-08 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_product_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('N', 'None'), ('E', 'Electronics'), ('F', 'Furnitures'), ('H', 'Houseware'), ('T', 'Toys'), ('B', 'Books')], default='N', max_length=1),
        ),
        migrations.AddField(
            model_name='product',
            name='label',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8),
        ),
    ]
