# Generated by Django 3.1.4 on 2021-02-28 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0013_resetrequest'),
    ]

    operations = [
        migrations.AddField(
            model_name='resetrequest',
            name='password',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='resetrequest',
            name='code',
            field=models.CharField(blank=True, max_length=12),
        ),
    ]
