# Generated by Django 3.0.1 on 2021-01-25 15:22

import django.core.validators
from django.db import migrations, models
import shop.models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0043_contactus_mobile'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='search_tags',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='manfacturedate',
            name='manfacture_year',
            field=models.IntegerField(null=True, unique=True, validators=[django.core.validators.MinValueValidator(1890), shop.models.max_value_current_year], verbose_name='year'),
        ),
    ]
