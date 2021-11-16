# Generated by Django 3.2.9 on 2021-11-16 03:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0004_product'),
    ]

    operations = [
        migrations.CreateModel(
            name='certificate',
            fields=[
                ('certNumber', models.IntegerField(primary_key=True, serialize=False)),
                ('certID', models.IntegerField()),
                ('reportnumber', models.IntegerField()),
                ('locationID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.location')),
                ('modelnumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.product')),
                ('standardID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.test_standard')),
                ('userID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend.user')),
            ],
        ),
    ]
