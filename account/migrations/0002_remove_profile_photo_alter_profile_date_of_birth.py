# Generated by Django 5.0.9 on 2024-10-31 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='photo',
        ),
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]