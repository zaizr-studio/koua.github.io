# Generated by Django 4.0.6 on 2022-08-08 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('N', 'None'), ('E', 'Electronics'), ('F', 'Furnitures'), ('H', 'Houseware'), ('T', 'Toys'), ('B', 'Books')], default='N', max_length=1),
        ),
    ]