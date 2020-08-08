# Generated by Django 3.0.4 on 2020-08-08 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Committie', '0002_auto_20200807_2356'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='committie',
            name='Quote',
        ),
        migrations.AddField(
            model_name='committie',
            name='Instagram',
            field=models.URLField(blank=True),
        ),
        migrations.AddField(
            model_name='committie',
            name='Twitter',
            field=models.URLField(blank=True),
        ),
        migrations.AlterField(
            model_name='committie',
            name='Designation',
            field=models.CharField(choices=[('Incharge', 'Incharge'), ('Staff Coordinator', 'Staff Coordinator'), ('President', 'President'), ('Vice President', 'Vice President'), ('Secretary', 'Secretary'), ('Joint Secretary', 'Joint Secretary'), ('Sponsorship Head', ' Sponsorship Head'), ('Joint Sponsorship Head', 'Joint Sponsorship Head'), ('PR Head', 'PR Head'), ('Joint PR Head', 'Joint PR Head'), ('Creative Head', 'Creative Head'), ('Joint Creative Head', 'Joint Creative Head'), ('Technical Head', 'Technical Head'), ('Joint Technical Head', 'Joint Technical Head'), ('Organizing Head', 'Organizing Head'), ('Joint Organizing Head', 'Joint Organizing Head'), ('Magazine Head', 'Magazine Head'), ('Joint Magazine', 'Joint Magazine'), ('Treasurer', 'Treasurer'), ('Joint Treasurer', 'Joint Treasurer')], default='', max_length=50),
        ),
        migrations.AlterField(
            model_name='committie',
            name='Linkedin',
            field=models.URLField(blank=True),
        ),
    ]
