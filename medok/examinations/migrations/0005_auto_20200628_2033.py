# Generated by Django 3.0.5 on 2020-06-28 20:33

from django.db import migrations, models
import examinations.validators


class Migration(migrations.Migration):

    dependencies = [
        ('examinations', '0004_auto_20200628_1952'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='diastole',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[examinations.validators.validate_diastole_range], verbose_name='Ciśnienie Rozkurczowe'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='faeces',
            field=models.PositiveSmallIntegerField(blank=True, null=True, verbose_name='Stolec'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='pulse',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[examinations.validators.validate_pulse_range], verbose_name='Tętno'),
        ),
        migrations.AlterField(
            model_name='examination',
            name='systole',
            field=models.PositiveSmallIntegerField(blank=True, null=True, validators=[examinations.validators.validate_systole_range], verbose_name='Ciśnienie Skurczowe'),
        ),
    ]
