# Generated by Django 3.1.4 on 2021-02-26 05:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_profile_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='verified',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
