# Generated by Django 5.1 on 2024-09-27 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0021_color_hex_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='color',
            name='hex_value',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
