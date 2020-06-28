from django.forms import ModelForm

from .models import Examination


class ExaminationForm(ModelForm):
    class Meta:
        model = Examination
        fields = [
            "temperature",
            "pulse",
            "systole",
            "diastole",
            "diet",
            "faeces",
        ]


class DietForm(ExaminationForm):
    class Meta:
        model = Examination
        fields = [
            "diet",
        ]


class PressureForm(ExaminationForm):
    class Meta:
        model = Examination
        fields = [
            "systole",
            "diastole",
        ]


class PulseForm(ExaminationForm):
    class Meta:
        model = Examination
        fields = [
            "pulse",
        ]


class TemperatureForm(ExaminationForm):
    class Meta:
        model = Examination
        fields = [
            "temperature",
        ]
