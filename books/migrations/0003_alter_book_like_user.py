# Generated by Django 3.2.13 on 2022-12-03 18:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0002_rename_like_users_book_like_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='like_user',
            field=models.ManyToManyField(related_name='books', to=settings.AUTH_USER_MODEL),
        ),
    ]
