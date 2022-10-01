# Generated by Django 3.0.1 on 2021-07-06 08:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0053_auto_20210703_1637'),
        ('main', '0009_auto_20210408_0843'),
    ]

    operations = [
        migrations.CreateModel(
            name='Offer_category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('name_arabic', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Offer_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('valid_from', models.DateField()),
                ('valid_to', models.DateField()),
                ('offer_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Offer_category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='shop.Product')),
            ],
        ),
    ]
