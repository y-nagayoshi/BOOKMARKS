# Generated by Django 5.0.9 on 2024-10-31 23:56

import account.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_delete_testlist'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestList',
            fields=[
                ('id', models.CharField(max_length=6, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=50)),
                # ('testdate', account.models.TimestampWithTimeZoneField()),
                ('size', models.IntegerField()),
            ],
        ),
    ]
