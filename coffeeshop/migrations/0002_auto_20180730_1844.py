# Generated by Django 2.0.7 on 2018-07-30 10:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coffeeshop', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2018, 7, 30, 18, 44, 17, 596787)),
        ),
    ]