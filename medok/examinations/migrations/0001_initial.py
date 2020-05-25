# Generated by Django 3.0.5 on 2020-05-25 15:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='PulseExamination',
            fields=[
                ('examination_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='examinations.Examination')),
                ('pulse', models.PositiveSmallIntegerField(verbose_name='Tętno')),
            ],
            options={
                'abstract': False,
            },
            bases=('examinations.examination',),
        ),
        migrations.CreateModel(
            name='TemperatureExamination',
            fields=[
                ('examination_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='examinations.Examination')),
                ('temperature', models.DecimalField(decimal_places=1, max_digits=3, verbose_name='Temperatura')),
            ],
            options={
                'abstract': False,
            },
            bases=('examinations.examination',),
        ),
    ]
