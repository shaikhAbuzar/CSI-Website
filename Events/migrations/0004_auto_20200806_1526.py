# Generated by Django 3.0.4 on 2020-08-06 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Events', '0003_auto_20200806_1525'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(max_length=2500),
        ),
    ]
