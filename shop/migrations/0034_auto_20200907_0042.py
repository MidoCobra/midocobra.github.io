# Generated by Django 3.0.8 on 2020-09-06 21:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0033_auto_20200906_1834'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='model',
            name='slug',
            field=models.SlugField(max_length=100, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='slug',
            field=models.SlugField(help_text='This field will be filled automatically', max_length=100, unique=True),
        ),
    ]
