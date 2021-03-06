# Generated by Django 3.1.4 on 2021-02-17 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('items', '0007_auto_20210216_1623'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='returned',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='order',
            name='returned_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='order',
            name='count',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='order',
            name='day',
            field=models.IntegerField(default=7),
        ),
    ]
