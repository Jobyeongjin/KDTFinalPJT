# Generated by Django 3.2.13 on 2022-12-05 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20221205_1441'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='detail_place',
            field=models.CharField(default='모임장소', max_length=200),
        ),
    ]