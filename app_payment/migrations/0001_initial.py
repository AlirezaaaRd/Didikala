# Generated by Django 5.1 on 2024-09-09 07:26

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mainapp', '0004_remove_address_user_remove_baseproduct_brand_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(choices=[(False, 'Failed'), (True, 'Success')], default=False)),
                ('ref_code', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Basket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='BasketItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('basket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_payment.basket')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.digitalproduct')),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('transaction', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='app_payment.transaction')),
            ],
        ),
        migrations.CreateModel(
            name='OrderItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.IntegerField()),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_payment.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.digitalproduct')),
            ],
        ),
    ]
