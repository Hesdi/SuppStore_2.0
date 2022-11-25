# Generated by Django 4.1.3 on 2022-11-25 10:45

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 25, 10, 45, 8, 471695, tzinfo=datetime.timezone.utc), verbose_name='Product Date'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_price',
            field=models.IntegerField(verbose_name='Product Price'),
        ),
    ]
