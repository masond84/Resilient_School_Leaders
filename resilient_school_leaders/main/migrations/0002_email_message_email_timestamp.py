# Generated by Django 4.2 on 2023-05-27 13:55

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='message',
            field=models.TextField(default='No Message'),
        ),
        migrations.AddField(
            model_name='email',
            name='timestamp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]
