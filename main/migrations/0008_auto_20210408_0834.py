# Generated by Django 3.0.1 on 2021-04-08 05:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_photosuploader'),
    ]

    operations = [
        migrations.CreateModel(
            name='HomePage_main_banners_WEBSITE',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('link_english', models.URLField()),
                ('link_arabic', models.URLField()),
                ('banner_title', models.CharField(max_length=154)),
                ('search_key', models.CharField(max_length=154, null=True)),
                ('banner_image', models.ImageField(upload_to='media/', verbose_name='Photo 1920x720')),
            ],
        ),
        migrations.DeleteModel(
            name='Products_Photo_Uploader',
        ),
        migrations.DeleteModel(
            name='Products_Photo_Uploader_2',
        ),
        migrations.AlterField(
            model_name='photosuploader',
            name='file',
            field=models.ImageField(upload_to='media/'),
        ),
    ]
