# Generated by Django 4.1.3 on 2022-12-15 10:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0014_alter_product_prod_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prod_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 15, 10, 55, 40, 856942, tzinfo=datetime.timezone.utc), verbose_name='Product Date'),
        ),
    ]