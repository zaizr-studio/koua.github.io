# Generated by Django 4.0.6 on 2022-08-08 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_product_category_product_label_product_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('None', 'N'), ('Electronics', 'E'), ('Furnitures', 'F'), ('Houseware', 'H'), ('Toys', 'T'), ('Books', 'B')], default='N', max_length=11),
        ),
    ]
