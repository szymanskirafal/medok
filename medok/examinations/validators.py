from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_diastole_range(value):
    if value > 240:
        raise ValidationError(
            _("Podane ciśnienie jest za wysokie"), params={"value": value},
        )
    if value < 70:
        raise ValidationError(
            _("Podane ciśnienie jest za niskie"), params={"value": value},
        )


def validate_systole_range(value):
    if value > 200:
        raise ValidationError(
            _("Podane ciśnienie jest za wysokie"), params={"value": value},
        )
    if value < 40:
        raise ValidationError(
            _("Podane ciśnienie jest za niskie"), params={"value": value},
        )


def validate_pulse_range(value):
    if value > 150:
        raise ValidationError(
            _("Podany puls jest za wysoki"), params={"value": value},
        )
    if value < 40:
        raise ValidationError(
            _("Podany puls jest za niski"), params={"value": value},
        )


def validate_temperature_range(value):
    if value >= 42:
        raise ValidationError(
            _("Podana temperatura jest za wysoka"), params={"value": value},
        )
    if value < 35:
        raise ValidationError(
            _("Podana temperatura jest za niska"), params={"value": value},
        )
