# Generated by Django 4.2.3 on 2023-12-27 07:03

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_car_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='logs',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='review',
            name='show',
            field=models.BooleanField(default=False),
        ),
    ]
