# Generated by Django 3.1.5 on 2021-01-28 08:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetmap', '0004_myosm_titre'),
    ]

    operations = [
        migrations.AddField(
            model_name='myosm',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='myosm',
            name='email',
            field=models.EmailField(blank=True, max_length=254),
        ),
        migrations.AddField(
            model_name='myosm',
            name='phone',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='myosm',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='myosm',
            name='titre',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
