# Generated by Django 3.2.13 on 2022-12-14 02:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0002_alter_group_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='number',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(3)]),
        ),
    ]
