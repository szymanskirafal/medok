from django.db import models
from patients.models import Patient

from medok.users.models import User

from .validators import (
    validate_diastole_range,
    validate_pulse_range,
    validate_systole_range,
    validate_temperature_range,
)


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Examination(TimeStampedModel):
    LIQUID = "LI"
    YES = "YE"
    NO = "NO"
    TYPE_OF_DIET = [
        (LIQUID, "Płynna"),
        (YES, "Tak"),
        (NO, "Nie"),
    ]
    made_on = models.DateTimeField(auto_now_add=False, editable=True)
    done_by = models.ForeignKey(User, on_delete=models.CASCADE,)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,)
    day_shift = models.BooleanField(default=False)
    night_shift = models.BooleanField(default=False)
    additional = models.BooleanField(default=False)
    temperature = models.DecimalField(
        null=False,
        blank=False,
        max_digits=3,
        decimal_places=1,
        verbose_name="Temperatura",
        validators=[validate_temperature_range],
    )
    pulse = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[validate_pulse_range],
        verbose_name="Tętno",
    )
    systole = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[validate_systole_range],
        verbose_name="Ciśnienie Skurczowe",
    )
    diastole = models.PositiveSmallIntegerField(
        null=False,
        blank=False,
        validators=[validate_diastole_range],
        verbose_name="Ciśnienie Rozkurczowe",
    )
    diet = models.CharField(
        max_length=2, choices=TYPE_OF_DIET, default=NO, verbose_name="Dieta",
    )
    faeces = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Stolec",
    )

    # def __str__(self):
    #    return self.get_diet_display()
