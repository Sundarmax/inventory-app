# Generated by Django 4.0.4 on 2022-05-13 14:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_of_order', models.DateField()),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='customer.customer')),
            ],
        ),
    ]
