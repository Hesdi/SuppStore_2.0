# Generated by Django 4.1.3 on 2022-12-15 04:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_product_prod_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 4, 20, 26, 956795, tzinfo=datetime.timezone.utc), verbose_name='Product Date'),
        ),
    ]
