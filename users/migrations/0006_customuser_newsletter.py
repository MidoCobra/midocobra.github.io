# Generated by Django 3.0.8 on 2020-08-27 03:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_auto_20200827_0023'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='newsLetter',
            field=models.BooleanField(default=False),
        ),
    ]
