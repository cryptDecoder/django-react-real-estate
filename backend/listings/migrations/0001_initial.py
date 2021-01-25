# Generated by Django 3.1.5 on 2021-01-24 16:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.CharField(max_length=100, unique=True)),
                ('title', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=15)),
                ('description', models.CharField(max_length=250)),
                ('sale_type', models.CharField(choices=[('FOR_SALE', 'FOR_SALE'), ('FOR_RENT', 'FOR_RENT')], default='FOR_SALE', max_length=100)),
                ('price', models.IntegerField()),
                ('bedrooms', models.IntegerField()),
                ('bathrooms', models.DecimalField(decimal_places=1, max_digits=2)),
                ('home_types', models.CharField(choices=[('HOUSE', 'HOUSE'), ('CONDO', 'CONDO'), ('TOWNHOUSE', 'TOWNHOUSE')], default='HOUSE', max_length=100)),
                ('sqft', models.IntegerField()),
                ('open_house', models.BooleanField(default=False)),
                ('photo_1', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_2', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_3', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_4', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_5', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_6', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_7', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_8', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_9', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_10', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_11', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_12', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_13', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_14', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_15', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_17', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_18', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_19', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_20', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_21', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('photo_22', models.ImageField(blank=True, upload_to='photo/%y/%m/%d/')),
                ('is_publish', models.BooleanField(default=True)),
                ('list_date', models.DateTimeField(blank=True, default=django.utils.timezone.now)),
                ('realtor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='realtors.realtor')),
            ],
        ),
    ]
