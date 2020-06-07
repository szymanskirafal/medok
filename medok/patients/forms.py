from django.forms import ModelForm, TextInput

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
        widgets = {
            "birthday": TextInput(attrs={"placeholder": "1950-03-08"}),
        }
