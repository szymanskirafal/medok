from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views import generic
from patients.models import Patient
from patients.utils import check_shift

from .forms import (
    FaecesExaminationForm,
    PressureExaminationForm,
    PulseExaminationForm,
    TemperatureExaminationForm,
)
from .models import (
    FaecesExamination,
    PressureExamination,
    PulseExamination,
    TemperatureExamination,
)


class FaecesExaminationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = FaecesExaminationForm
    model = FaecesExamination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class PressureExaminationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PressureExaminationForm
    model = PressureExamination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class PulseExaminationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PulseExaminationForm
    model = PulseExamination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class TemperatureExaminationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = TemperatureExaminationForm
    model = TemperatureExamination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        shift = check_shift()
        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})
