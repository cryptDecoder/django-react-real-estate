# Generated by Django 3.1.5 on 2021-01-24 20:22

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='message',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='contact_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime.now),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='contacts',
            name='subject',
            field=models.CharField(max_length=100),
        ),
    ]
