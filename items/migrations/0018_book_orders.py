# Generated by Django 3.1.4 on 2021-02-24 09:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0017_auto_20210222_1848'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='orders',
            field=models.IntegerField(default=0),
        ),
    ]