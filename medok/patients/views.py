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
from .utils import check_shift


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

    def need_for_diet_recommendation(self, **kwargs):
        examinations = DietRecommendation.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        examinations = examinations.filter(additional=False)
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_faeces_examination(self, **kwargs):
        examinations = FaecesExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        examinations = examinations.filter(additional=False)
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_pressure_examination(self, **kwargs):
        examinations = PressureExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        examinations = examinations.filter(additional=False)
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_pulse_examination(self, **kwargs):
        examinations = PulseExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        examinations = examinations.filter(additional=False)
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def need_for_temperature_examination(self, **kwargs):
        examinations = TemperatureExamination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(created__date=date.today(),)
        examinations = examinations.filter(additional=False)
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def get_shift_name(self):
        shift = check_shift()
        if shift == "night":
            shift_name = "Wieczorny"
        else:
            shift_name = "Ranny"
        return shift_name

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.need_for_diet_recommendation():
            context["diet_form"] = DietRecommendationForm()
        if self.need_for_faeces_examination():
            context["faeces_form"] = FaecesExaminationForm()
        if self.need_for_pressure_examination():
            context["pressure_form"] = PressureExaminationForm()
        if self.need_for_pulse_examination():
            context["pulse_form"] = PulseExaminationForm()
        if self.need_for_temperature_examination():
            context["temperature_form"] = TemperatureExaminationForm()
        context["shift_name"] = self.get_shift_name()
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
            shift = check_shift()
            if shift == "night":
                night_shift = True
                day_shift = False
            else:
                night_shift = False
                day_shift = True
            DietRecommendation.objects.create(
                made_by=self.request.user,
                patient=self.object,
                diet=diet_form.cleaned_data["diet"],
                day_shift=day_shift,
                night_shift=night_shift,
            )
            return self.form_valid(diet_form)

        faeces_form = self.get_form(form_class=self.faeces_form_class)
        if faeces_form.is_valid():
            shift = check_shift()
            if shift == "night":
                night_shift = True
                day_shift = False
            else:
                night_shift = False
                day_shift = True
            FaecesExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                faeces=faeces_form.cleaned_data["faeces"],
                day_shift=day_shift,
                night_shift=night_shift,
            )
            return self.form_valid(faeces_form)

        pressure_form = self.get_form(form_class=self.pressure_form_class)
        if pressure_form.is_valid():
            shift = check_shift()
            if shift == "night":
                night_shift = True
                day_shift = False
            else:
                night_shift = False
                day_shift = True

            PressureExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                systole=pressure_form.cleaned_data["systole"],
                diastole=pressure_form.cleaned_data["diastole"],
                day_shift=day_shift,
                night_shift=night_shift,
            )
            return self.form_valid(pressure_form)

        pulse_form = self.get_form(form_class=self.pulse_form_class)
        if pulse_form.is_valid():
            shift = check_shift()
            if shift == "night":
                night_shift = True
                day_shift = False
            else:
                night_shift = False
                day_shift = True

            PulseExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                pulse=pulse_form.cleaned_data["pulse"],
                day_shift=day_shift,
                night_shift=night_shift,
            )
            return self.form_valid(pulse_form)

        temperature_form = self.get_form(form_class=self.temperature_form_class)
        if temperature_form.is_valid():
            shift = check_shift()
            if shift == "night":
                night_shift = True
                day_shift = False
            else:
                night_shift = False
                day_shift = True

            TemperatureExamination.objects.create(
                made_by=self.request.user,
                patient=self.object,
                temperature=temperature_form.cleaned_data["temperature"],
                day_shift=day_shift,
                night_shift=night_shift,
            )
            return self.form_valid(temperature_form)
        else:
            return self.form_invalid(temperature_form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.object.pk})


class PatientsListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "patients"
    model = Patient
    template_name = "patients/patients.html"
