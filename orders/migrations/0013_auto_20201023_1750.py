# Generated by Django 3.0.1 on 2020-10-23 14:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0012_auto_20201023_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='country',
            field=models.CharField(blank=True, default='Egypt', max_length=100),
        ),
    ]
