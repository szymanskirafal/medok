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
    DietRecommendation,
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


class DietRecommendationHistoricalListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = DietRecommendation
    template_name = "examinations/historical-diet.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return DietRecommendation.objects.all().filter(patient=self.patient)


class FaecesExaminationHistoricalListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = FaecesExamination
    template_name = "examinations/historical-faeces.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return FaecesExamination.objects.all().filter(patient=self.patient)


class PressureExaminationHistoricalListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = PressureExamination
    template_name = "examinations/historical-pressure.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return PressureExamination.objects.all().filter(patient=self.patient)


class PulseExaminationHistoricalListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = PulseExamination
    template_name = "examinations/historical-pulse.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return PulseExamination.objects.all().filter(patient=self.patient)


class TemperatureExaminationHistoricalListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = TemperatureExamination
    template_name = "examinations/historical-temperature.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return TemperatureExamination.objects.all().filter(patient=self.patient)
