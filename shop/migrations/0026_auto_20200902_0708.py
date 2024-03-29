# Generated by Django 3.0.8 on 2020-09-02 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0025_auto_20200901_0745'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='slug',
            field=models.SlugField(help_text='This field will be filled automatically', max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='blog',
            name='title',
            field=models.TextField(db_index=True, max_length=300),
        ),
    ]
