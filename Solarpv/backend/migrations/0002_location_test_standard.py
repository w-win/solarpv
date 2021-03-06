# Generated by Django 3.2.9 on 2021-11-16 03:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='test_standard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('standardname', models.CharField(max_length=20)),
                ('description', models.CharField(max_length=50)),
                ('publishDate', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='location',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('address1', models.CharField(max_length=50)),
                ('address2', models.CharField(max_length=10)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=2)),
                ('postalcode', models.IntegerField()),
                ('country', models.CharField(max_length=50)),
                ('pnumber', models.CharField(max_length=20)),
                ('faxnumber', models.CharField(max_length=20)),
                ('location_client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.client')),
            ],
        ),
    ]
