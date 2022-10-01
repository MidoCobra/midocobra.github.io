# Generated by Django 3.0.1 on 2021-07-13 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0054_auto_20210713_1611'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='rim_size',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tire_height',
        ),
        migrations.RemoveField(
            model_name='product',
            name='tire_width',
        ),
        migrations.AddField(
            model_name='product',
            name='tire_height_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Tire_height'),
        ),
        migrations.AddField(
            model_name='product',
            name='tire_rim_size',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Rim_size'),
        ),
        migrations.AddField(
            model_name='product',
            name='tire_width_num',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='shop.Tire_width'),
        ),
    ]
