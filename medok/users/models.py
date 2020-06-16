from django.contrib.auth.models import AbstractUser
from django.core import validators
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name of User"), blank=True, max_length=255)
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
    nurse = models.BooleanField("Pielęgniarka", default=True)
    doctor = models.BooleanField("Lekarz", default=False)
    psychologist = models.BooleanField("Psycholog", default=False)
    physiotherapist = models.BooleanField("Fizjoterapeuta", default=False)
    occupational_therapist = models.BooleanField("Terapeuta zabiegowy", default=False)
    superuser = models.BooleanField(_("Superuser"), default=False)

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
