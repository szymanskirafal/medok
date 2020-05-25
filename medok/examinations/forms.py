from django.forms import ModelForm

from .models import (
    DietRecommendation,
    FaecesExamination,
    PressureExamination,
    PulseExamination,
    TemperatureExamination,
)


class DietRecommendationForm(ModelForm):
    class Meta:
        model = DietRecommendation
        fields = [
            "diet",
        ]


class FaecesExaminationForm(ModelForm):
    class Meta:
        model = FaecesExamination
        fields = [
            "faeces",
        ]


class PressureExaminationForm(ModelForm):
    class Meta:
        model = PressureExamination
        fields = [
            "systole",
            "diastole",
        ]


class TemperatureExaminationForm(ModelForm):
    class Meta:
        model = TemperatureExamination
        fields = [
            "temperature",
        ]


class PulseExaminationForm(ModelForm):
    class Meta:
        model = PulseExamination
        fields = [
            "pulse",
        ]
