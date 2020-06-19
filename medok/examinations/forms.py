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
