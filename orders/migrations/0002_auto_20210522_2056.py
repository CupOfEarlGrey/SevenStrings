# Generated by Django 3.2.2 on 2021-05-22 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='apartment',
            field=models.CharField(default=None, max_length=50),
        ),
        migrations.AddField(
            model_name='order',
            name='country',
            field=models.CharField(default=None, max_length=250),
        ),
        migrations.AddField(
            model_name='order',
            name='phone',
            field=models.IntegerField(default=0, verbose_name=10),
        ),
        migrations.AddField(
            model_name='order',
            name='street',
            field=models.CharField(default=None, max_length=250),
        ),
    ]
