# Generated by Django 2.0.13 on 2020-03-05 01:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0120_auto_20200303_1506'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='condition',
            field=models.CharField(blank=True, default='', max_length=200),
        ),
    ]