# Generated by Django 4.0.4 on 2022-05-29 16:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviadb', '0018_alter_aircraft_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='aircraft',
            name='photo',
            field=models.ImageField(upload_to='media'),
        ),
    ]