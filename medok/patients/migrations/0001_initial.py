# Generated by Django 3.0.5 on 2020-06-18 18:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50, verbose_name='Imię')),
                ('surname', models.CharField(max_length=100, verbose_name='Nazwisko')),
                ('pesel', models.BigIntegerField(validators=[django.core.validators.MinValueValidator(10000000000), django.core.validators.MaxValueValidator(99999999999)], verbose_name='PESEL')),
                ('street', models.CharField(blank=True, max_length=100, verbose_name='Ulica')),
                ('nr', models.PositiveSmallIntegerField(blank=True, verbose_name='Numer')),
                ('zip_code', models.CharField(blank=True, max_length=6, verbose_name='Kod pocztowy')),
                ('city', models.CharField(blank=True, max_length=100, verbose_name='Miejscowość')),
                ('birthday', models.DateField(blank=True, verbose_name='Data urodzenia')),
                ('nr_in_main_book', models.CharField(blank=True, max_length=100, verbose_name='Numer w Książce Głównej')),
                ('nr_in_ward_book', models.CharField(blank=True, max_length=100, verbose_name='Numer w Książce Oddziałowej')),
                ('agreed_to_tests', models.BooleanField(default=False, verbose_name='Zgoda na wykonanie badań')),
            ],
        ),
    ]
