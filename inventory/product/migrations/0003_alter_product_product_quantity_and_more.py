# Generated by Django 4.0.4 on 2022-05-05 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='product_quantity',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='product_status',
            field=models.IntegerField(),
        ),
    ]