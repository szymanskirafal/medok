# Generated by Django 3.0.5 on 2020-06-28 19:50

from django.db import migrations, models
import examinations.validators


class Migration(migrations.Migration):

    dependencies = [
        ('examinations', '0002_auto_20200618_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examination',
            name='temperature',
            field=models.DecimalField(decimal_places=1, max_digits=3, null=True, validators=[examinations.validators.validate_temperature_range], verbose_name='Temperatura'),
        ),
    ]
