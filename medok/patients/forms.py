from django.forms import ModelForm

from .models import Patient


class PatientForm(ModelForm):
    class Meta:
        model = Patient
        fields = [
            "name",
            "surname",
            "pesel",
            "street",
            "nr",
            "zip_code",
            "city",
            "birthday",
            "nr_in_main_book",
            "nr_in_ward_book",
            "agreed_to_tests",
        ]
