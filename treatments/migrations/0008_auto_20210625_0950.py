# Generated by Django 3.2.3 on 2021-06-25 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('treatments', '0007_alter_treatment_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='treatment',
            name='name',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='treatment',
            name='sku',
            field=models.CharField(default=1, max_length=12),
            preserve_default=False,
        ),
    ]