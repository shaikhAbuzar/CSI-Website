# Generated by Django 3.0.4 on 2020-08-06 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='report_link',
            field=models.URLField(blank=True),
        ),
    ]
