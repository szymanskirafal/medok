from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class User(AbstractUser):

    # First Name and Last Name do not cover name patterns
    # around the globe.
    name = models.CharField(_("Name"), null=False, blank=False, max_length=255,)
    surname = models.CharField(_("Surname"), null=False, blank=False, max_length=255,)
    pesel = models.BigIntegerField(
        _("PESEL"), null=False, blank=False, min_length=11, max_length=11,
    )
    nurse = models.BooleanField(_("Nurse"), default=True)
    doctor = models.BooleanField(_("Doctor"), default=False)
    psychologist = models.BooleanField(_("Psychologist"), default=False)
    physiotherapist = models.BooleanField(_("Physiotherapist"), default=False)
    occupational_therapist = models.BooleanField(
        _("Occupational therapist"), default=False
    )

    def get_absolute_url(self):
        return reverse("users:detail", kwargs={"username": self.username})
