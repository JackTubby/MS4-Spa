# Generated by Django 3.2.3 on 2021-06-27 22:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0010_treatment_length'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='treatment',
            name='length',
        ),
    ]
