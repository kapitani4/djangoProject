# Generated by Django 4.0.3 on 2022-04-10 09:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviadb', '0004_alter_aircraft_options_alter_compartments_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='compartments',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='aviadb.compartments'),
        ),
    ]
