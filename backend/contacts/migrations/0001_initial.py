# Generated by Django 3.1.5 on 2021-01-24 20:02

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100)),
                ('subject', models.CharField(max_length=200)),
                ('contact_date', models.DateField(blank=True, default=datetime.datetime.now)),
            ],
        ),
    ]
