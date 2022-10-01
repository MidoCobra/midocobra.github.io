# Generated by Django 3.0.8 on 2020-08-31 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_auto_20200828_1620'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='youtube_link',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='seller_recommendation',
            field=models.BooleanField(default=False),
        ),
    ]
