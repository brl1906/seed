# Generated by Django 2.0.13 on 2020-03-03 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('seed', '0119_rule_condition'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rule',
            name='condition',
            field=models.CharField(default='', max_length=200),
        ),
    ]