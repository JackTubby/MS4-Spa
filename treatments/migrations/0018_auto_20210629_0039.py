# Generated by Django 3.2.3 on 2021-06-29 00:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0017_auto_20210628_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='hours',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='minutes',
            field=models.IntegerField(default=0),
        ),
    ]