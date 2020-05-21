from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views import generic

from .forms import PatientForm
from .models import Patient


class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PatientForm
    model = Patient
    success_url = reverse_lazy("patients:list")
    template_name = "patients/create.html"


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    context_object_name = "patient"
    model = Patient
    template_name = "patients/detail.html"


class PatientsListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "patients"
    model = Patient
    template_name = "patients/list.html"
