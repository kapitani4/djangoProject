# Generated by Django 4.0.3 on 2022-04-10 09:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('aviadb', '0009_alter_drawing_detail'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='drawing',
            name='detail',
        ),
    ]
