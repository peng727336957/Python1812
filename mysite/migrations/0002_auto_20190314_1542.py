# Generated by Django 2.1.7 on 2019-03-14 07:42

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment',
            name='nickname',
        ),
        migrations.AlterField(
            model_name='post',
            name='publish',
            field=models.DateTimeField(default=datetime.datetime(2019, 3, 14, 7, 42, 4, 796728, tzinfo=utc)),
        ),
    ]
