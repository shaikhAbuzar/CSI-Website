# Generated by Django 3.0.4 on 2020-08-08 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Committie', '0005_auto_20200808_1534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committie',
            name='Instagram',
        ),
        migrations.RemoveField(
            model_name='committie',
            name='Twitter',
        ),
    ]
