# Generated by Django 4.1.3 on 2022-12-15 04:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_profile_orders'),
        ('main', '0011_alter_product_prod_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.CharField(max_length=120)),
                ('order_id', models.CharField(max_length=120)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=100)),
                ('success', models.BooleanField(default=True)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.profile')),
            ],
            options={
                'ordering': ['-timestamp'],
            },
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now=True)),
                ('date_ordered', models.DateTimeField(null=True)),
                ('product', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='main.product')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ref_code', models.CharField(max_length=15)),
                ('is_ordered', models.BooleanField(default=False)),
                ('date_ordered', models.DateTimeField(auto_now=True)),
                ('items', models.ManyToManyField(to='shopping_cart.orderitem')),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.profile')),
            ],
        ),
    ]
