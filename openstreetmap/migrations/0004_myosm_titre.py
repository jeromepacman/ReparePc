# Generated by Django 3.1.5 on 2021-01-27 13:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetmap', '0003_auto_20210126_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='myosm',
            name='titre',
            field=models.CharField(default=django.utils.timezone.now, max_length=50),
            preserve_default=False,
        ),
    ]
