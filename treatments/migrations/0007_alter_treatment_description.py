# Generated by Django 3.2.3 on 2021-06-25 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0006_auto_20210620_1446'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='description',
            field=models.TextField(max_length=200),
        ),
    ]
