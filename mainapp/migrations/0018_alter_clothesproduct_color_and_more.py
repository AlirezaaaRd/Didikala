# Generated by Django 5.1 on 2024-09-22 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0017_remove_color_product_clothesproduct_color_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clothesproduct',
            name='color',
            field=models.ManyToManyField(null=True, to='mainapp.color'),
        ),
        migrations.AlterField(
            model_name='digitalproduct',
            name='color',
            field=models.ManyToManyField(null=True, to='mainapp.color'),
        ),
    ]
