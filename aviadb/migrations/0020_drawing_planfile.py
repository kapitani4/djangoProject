# Generated by Django 4.0.4 on 2022-06-16 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aviadb', '0019_alter_aircraft_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='drawing',
            name='planFile',
            field=models.FileField(default='plan.jpg', upload_to='files'),
        ),
    ]
