# Generated by Django 3.2.2 on 2021-05-26 00:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_seven_strings', '0005_delete_acousticguitar'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='brand',
            field=models.CharField(default=None, max_length=100),
        ),
    ]
