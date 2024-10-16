# Generated by Django 5.1 on 2024-10-04 10:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_alter_color_hex_value'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clothesproduct',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='clothesproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='clothesproduct',
            name='color',
        ),
        migrations.RemoveField(
            model_name='digitalproduct',
            name='brand',
        ),
        migrations.RemoveField(
            model_name='digitalproduct',
            name='category',
        ),
        migrations.RemoveField(
            model_name='digitalproduct',
            name='color',
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, null=True)),
                ('price', models.PositiveIntegerField(null=True)),
                ('count', models.PositiveIntegerField(null=True)),
                ('name_EN', models.CharField(max_length=255, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='mainapp.brand')),
                ('category', models.ManyToManyField(to='mainapp.category')),
                ('color', models.ManyToManyField(to='mainapp.color')),
            ],
        ),
    ]
