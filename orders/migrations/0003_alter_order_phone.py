# Generated by Django 3.2.2 on 2021-05-25 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20210522_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=0, max_length=10),
        ),
    ]
