from django.core import validators
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Patient(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    name = models.CharField(_("Name"), blank=False, max_length=50)
    surname = models.CharField(_("Surname"), blank=False, max_length=100)
    pesel = models.BigIntegerField(
        _("PESEL"),
        null=False,
        blank=False,
        default=11223344555,
        validators=[
            validators.MinValueValidator(10000000000),
            validators.MaxValueValidator(99999999999),
        ],
    )
    street = models.CharField(_("Street"), blank=True, max_length=100)
    nr = models.PositiveSmallIntegerField(_("Number"), blank=True)
    zip_code = models.CharField(_("Zip Code"), blank=True, max_length=6)
    city = models.CharField(_("City"), blank=True, max_length=100)
    birthday = models.DateField(blank=True,)
    nr_in_main_book = models.PositiveSmallIntegerField(
        _("Number in The Main Book"), blank=True
    )
    nr_in_ward_book = models.PositiveSmallIntegerField(
        _("Number in The Ward Book"), blank=True
    )
    agreed_to_tests = models.BooleanField(_("Agreed to the tests"), default=False)

    def get_absolute_url(self):
        pass
