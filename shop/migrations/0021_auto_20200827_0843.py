# Generated by Django 3.0.8 on 2020-08-27 05:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0020_blog_blog_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='name_arabic',
            field=models.CharField(db_index=True, max_length=150, null=True),
        ),
        migrations.AddField(
            model_name='category',
            name='name_arabic',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='model',
            name='name_arabic',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='description_arabic',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='features_arabic',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='made_in_arabic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='name_arabic',
            field=models.CharField(max_length=100, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='product',
            name='product_commercial_name_arabic',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(db_index=True, max_length=150, unique=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='features',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(db_index=True, max_length=100, unique=True),
        ),
    ]
