# Generated by Django 2.0.7 on 2018-07-30 10:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Drink',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('type', models.CharField(max_length=100)),
                ('price_tall', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('price_grande', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('price_venti', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('orderId', models.IntegerField(default=0)),
                ('type', models.CharField(max_length=100)),
                ('item', models.CharField(max_length=100)),
                ('volume', models.IntegerField(default=0)),
                ('size', models.CharField(max_length=100)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10, null=True)),
                ('date', models.DateTimeField(default=datetime.datetime(2018, 7, 30, 18, 43, 39, 885652))),
            ],
        ),
    ]
