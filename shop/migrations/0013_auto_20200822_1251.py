# Generated by Django 3.0.8 on 2020-08-22 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_auto_20200818_0027'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='made_in',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_commercial_name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
