# Generated by Django 3.0.8 on 2020-08-24 22:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_category_category_leftside_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='image2',
        ),
        migrations.AlterField(
            model_name='product',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
    ]
