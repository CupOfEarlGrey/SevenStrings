# Generated by Django 3.2.2 on 2021-05-29 04:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_seven_strings', '0011_auto_20210529_0721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, upload_to='main_seven_strings/media/&Y/'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image_2',
            field=models.ImageField(blank=True, upload_to='main_seven_strings/media/&Y/'),
        ),
    ]
