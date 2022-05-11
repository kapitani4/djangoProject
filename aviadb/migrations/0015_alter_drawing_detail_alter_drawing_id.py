# Generated by Django 4.0.3 on 2022-04-10 10:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('aviadb', '0014_alter_drawing_detail'),
    ]

    operations = [
        migrations.AlterField(
            model_name='drawing',
            name='detail',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='aviadb.compartments'),
        ),
        migrations.AlterField(
            model_name='drawing',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
