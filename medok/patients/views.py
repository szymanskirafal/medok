from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseForbidden
from django.urls import reverse, reverse_lazy
from django.views import View, generic
from examinations.forms import (
    DietRecommendationForm,
    FaecesExaminationForm,
    PressureExaminationForm,
    PulseExaminationForm,
    TemperatureExaminationForm,
)
from examinations.models import (
    DietRecommendation,
    FaecesExamination,
    PressureExamination,
    PulseExamination,
    TemperatureExamination,
)

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


class PatientExaminationsDetailView(View):
    def get(self, request, *args, **kwargs):
        view = PatientExaminationsDisplayView.as_view()
        return view(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        view = PatientExaminationMadeView.as_view()
        return view(request, *args, **kwargs)


class PatientExaminationsDisplayView(LoginRequiredMixin, generic.DetailView):
    context_object_name = "patient"
    model = Patient
    template_name = "patients/examinations.html"

    def need_for_morning_diet_recommendation(self, **kwargs):
        recommendations = DietRecommendation.objects.all()
        recommendations = recommendations.filter(patient=self.get_object(),)
        recommendations = recommendations.filter(created__date=date.today(),)
        if recommendations.exists():
            return False
        else:
            return True

    def need_for_morning_faeces_examination(self, **kwargs):
        examinations = FaecesExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_morning_pressure_examination(self, **kwargs):
        examinations = PressureExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_morning_pulse_examination(self, **kwargs):
        examinations = PulseExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_morning_temperature_examination(self, **kwargs):
        temp_examinations = TemperatureExamination.objects.all()
        temp_examinations = temp_examinations.filter(patient=self.get_object(),)
        temp_examinations = temp_examinations.filter(created__date=date.today(),)
        if temp_examinations.exists():
            return False
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.need_for_morning_diet_recommendation():
            context["diet_form"] = DietRecommendationForm()
        if self.need_for_morning_faeces_examination():
            context["faeces_form"] = FaecesExaminationForm()
        if self.need_for_morning_temperature_examination():
            context["temperature_form"] = TemperatureExaminationForm()
        if self.need_for_morning_pressure_examination():
            context["pressure_form"] = PressureExaminationForm()
        if self.need_for_morning_pulse_examination():
            context["pulse_form"] = PulseExaminationForm()
        return context


class PatientExaminationMadeView(
    LoginRequiredMixin, generic.edit.FormMixin, generic.DetailView
):
    diet_form_class = DietRecommendationForm
    faeces_form_class = FaecesExaminationForm
    pressure_form_class = PressureExaminationForm
    pulse_form_class = PulseExaminationForm
    temperature_form_class = TemperatureExaminationForm
    model = Patient
    template_name = "patients/examinations.html"

    def post(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return HttpResponseForbidden()
        self.object = self.get_object()

        diet_form = self.get_form(form_class=self.diet_form_class)
        if diet_form.is_valid():
            DietRecommendation.objects.create(
                made_by=self.request.user,
                patient=self.object,
                diet=diet_form.cleaned_data["diet"],
            )
            return self.form_valid(diet_form)

        faeces_form = self.get_form(form_class=self.faeces_form_class)
        if faeces_form.is_valid():
            FaecesExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                faeces=faeces_form.cleaned_data["faeces"],
            )
            return self.form_valid(faeces_form)

        pressure_form = self.get_form(form_class=self.pressure_form_class)
        if pressure_form.is_valid():
            PressureExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                systole=pressure_form.cleaned_data["systole"],
                diastole=pressure_form.cleaned_data["diastole"],
            )
            return self.form_valid(pressure_form)

        pulse_form = self.get_form(form_class=self.pulse_form_class)
        if pulse_form.is_valid():
            PulseExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                pulse=pulse_form.cleaned_data["pulse"],
            )
            return self.form_valid(pulse_form)

        temperature_form = self.get_form(form_class=self.temperature_form_class)
        if temperature_form.is_valid():
            TemperatureExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                temperature=temperature_form.cleaned_data["temperature"],
            )
            return self.form_valid(temperature_form)

        else:
            return self.form_invalid(temperature_form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.object.pk})


class PatientsListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "patients"
    model = Patient
    template_name = "patients/list.html"
