# Generated by Django 3.1.5 on 2021-02-02 12:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openstreetmap', '0007_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myosm',
            name='address',
        ),
        migrations.RemoveField(
            model_name='myosm',
            name='zipcode',
        ),
    ]
