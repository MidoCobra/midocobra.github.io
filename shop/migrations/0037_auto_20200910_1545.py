# Generated by Django 3.0.8 on 2020-09-10 12:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0036_product_hidden'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact_information',
            name='phone3',
            field=models.CharField(max_length=220, verbose_name='Hotline'),
        ),
    ]
