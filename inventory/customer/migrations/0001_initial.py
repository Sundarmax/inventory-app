# Generated by Django 4.0.4 on 2022-05-13 14:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.IntegerField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=40)),
                ('last_name', models.CharField(max_length=40)),
                ('address', models.CharField(blank=True, max_length=120, null=True)),
                ('phone', models.IntegerField()),
                ('email', models.CharField(max_length=40)),
            ],
        ),
    ]
