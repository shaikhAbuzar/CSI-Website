# Generated by Django 3.0.4 on 2020-08-06 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0002_event_report_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=1000),
        ),
    ]
