# Generated by Django 4.1.3 on 2022-12-15 04:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0011_alter_product_prod_date'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='orders',
            field=models.ManyToManyField(blank=True, to='main.product'),
        ),
    ]