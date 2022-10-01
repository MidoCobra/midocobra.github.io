# Generated by Django 3.0.8 on 2020-09-06 11:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_product_modeltest'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact_information',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('physical_address1', models.CharField(max_length=220)),
                ('phone1', models.CharField(max_length=220)),
                ('phone2', models.CharField(max_length=220)),
                ('phone3', models.CharField(max_length=220)),
                ('email1', models.EmailField(max_length=254)),
                ('email2', models.EmailField(max_length=254)),
                ('working_hours', models.CharField(max_length=220)),
                ('physical_address1_arabic', models.CharField(max_length=220)),
                ('working_hours_arabic', models.CharField(max_length=220)),
                ('facebook_link', models.URLField()),
                ('instagram_link', models.URLField()),
                ('youtube_link', models.URLField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='modelTest',
        ),
    ]
