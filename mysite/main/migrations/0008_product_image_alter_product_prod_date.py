# Generated by Django 4.1.3 on 2022-12-14 04:18

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_product_category_alter_product_prod_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='default_prod.jpg', upload_to='product_pics'),
        ),
        migrations.AlterField(
            model_name='product',
            name='prod_date',
            field=models.DateTimeField(default=datetime.datetime(2022, 12, 14, 4, 18, 37, 339077, tzinfo=datetime.timezone.utc), verbose_name='Product Date'),
        ),
    ]