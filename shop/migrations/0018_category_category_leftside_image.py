# Generated by Django 3.0.8 on 2020-08-24 21:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_category_category_banner'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='category_leftSide_image',
            field=models.ImageField(null=True, upload_to='media/', verbose_name='photo 270x420'),
        ),
    ]
