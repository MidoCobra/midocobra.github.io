# Generated by Django 3.0.1 on 2020-10-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0042_contactus_created_at'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='mobile',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
