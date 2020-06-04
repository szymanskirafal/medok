from django.db import models
from patients.models import Patient

from medok.users.models import User


class TimeStampedModel(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Examination(TimeStampedModel):
    made_by = models.ForeignKey(User, on_delete=models.CASCADE,)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE,)
    day_shift = models.BooleanField(default=False)
    night_shift = models.BooleanField(default=False)
    additional = models.BooleanField(default=False)

    class Meta:
        abstract = True


class DietRecommendation(Examination):
    LIQUID = "LI"
    YES = "YE"
    NO = "NO"
    TYPE_OF_DIET = [
        (LIQUID, "Płynna"),
        (YES, "Tak"),
        (NO, "Nie"),
    ]
    diet = models.CharField(
        max_length=2, choices=TYPE_OF_DIET, default=NO, verbose_name="Dieta",
    )

    def __str__(self):
        return self.get_diet_display()


class FaecesExamination(Examination):
    faeces = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Stolec",
    )


class PressureExamination(Examination):
    systole = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Ciśnienie Skurczowe",
    )
    diastole = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Ciśnienie Rozkurczowe",
    )


class PulseExamination(Examination):
    pulse = models.PositiveSmallIntegerField(
        null=False, blank=False, verbose_name="Tętno",
    )


class TemperatureExamination(Examination):
    temperature = models.DecimalField(
        null=False,
        blank=False,
        max_digits=3,
        decimal_places=1,
        verbose_name="Temperatura",
    )
