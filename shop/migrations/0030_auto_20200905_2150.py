# Generated by Django 3.0.8 on 2020-09-05 18:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0029_auto_20200905_1437'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='model',
            field=models.ManyToManyField(related_name='partTypesModel', to='shop.Model'),
        ),
    ]
