from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(_("Imię"), blank=False, max_length=50)
    surname = models.CharField(_("Nazwisko"), blank=False, max_length=100)
    pesel = models.BigIntegerField(
        _("PESEL"),
        null=False,
        blank=False,
        # default=11223344555,
        validators=[
            validators.MinValueValidator(10000000000),
            validators.MaxValueValidator(99999999999),
        ],
    )
    street = models.CharField(_("Ulica"), blank=True, max_length=100)
    nr = models.PositiveSmallIntegerField(_("Numer"), blank=True)
    zip_code = models.CharField(_("Kod pocztowy"), blank=True, max_length=6)
    city = models.CharField(_("Miejscowość"), blank=True, max_length=100)
    birthday = models.DateField(_("Data urodzenia"), blank=True,)
    nr_in_main_book = models.CharField(
        _("Numer w Książce Głównej"), blank=True, max_length=100,
    )
    nr_in_ward_book = models.CharField(
        _("Numer w Książce Oddziałowej"), blank=True, max_length=100,
    )
    agreed_to_tests = models.BooleanField(_("Zgoda na wykonanie badań"), default=False)

    def get_absolute_url(self):
        pass
