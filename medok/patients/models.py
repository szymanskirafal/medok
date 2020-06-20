from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(_("Imię"), max_length=50)
    surname = models.CharField(_("Nazwisko"), max_length=100)
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
    street = models.CharField(_("Ulica"), max_length=100)
    nr = models.PositiveSmallIntegerField(_("Numer"),)
    zip_code = models.CharField(_("Kod pocztowy"), max_length=6)
    city = models.CharField(_("Miejscowość"), max_length=100)
    birthday = models.DateField(_("Data urodzenia"))
    nr_in_main_book = models.CharField(_("Numer w Książce Głównej"), max_length=100,)
    nr_in_ward_book = models.CharField(
        _("Numer w Książce Oddziałowej"), max_length=100,
    )
    agreed_to_tests = models.BooleanField(_("Zgoda na wykonanie badań"), default=False)

    def get_absolute_url(self):
        pass
