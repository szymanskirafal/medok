from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.urls import reverse
from django.utils import timezone
from django.views import generic
from patients.models import Patient
from patients.utils import get_current_shifts
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .forms import (
    DietForm,
    ExaminationForm,
    FaecesForm,
    PressureForm,
    PulseForm,
    TemperatureForm,
)
from .models import Examination


class ExaminationCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = ExaminationForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = False
        form.instance.temperature = form.cleaned_data["temperature"]
        form.instance.pulse = form.cleaned_data["pulse"]
        form.instance.systole = form.cleaned_data["systole"]
        form.instance.diastole = form.cleaned_data["diastole"]
        form.instance.diet = form.cleaned_data["diet"]
        form.instance.faeces = form.cleaned_data["faeces"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationAdditionalDietCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = DietForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        form.instance.diet = form.cleaned_data["diet"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationAdditionalFaecesCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = FaecesForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        form.instance.faeces = form.cleaned_data["faeces"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationAdditionalPressureCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PressureForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        form.instance.systole = form.cleaned_data["systole"]
        form.instance.diastole = form.cleaned_data["diastole"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationAdditionalTemperatureCreateView(
    LoginRequiredMixin, generic.CreateView
):
    form_class = TemperatureForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        form.instance.temperature = form.cleaned_data["temperature"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationAdditionalPulseCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PulseForm
    model = Examination
    template_name = "examinations/create.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = Patient.objects.get(pk=self.kwargs["pk"])
        return context

    def form_valid(self, form):
        form.instance.made_on = timezone.now()
        form.instance.done_by = self.request.user
        form.instance.patient = Patient.objects.get(pk=self.kwargs["pk"])
        day_shift, night_shift = get_current_shifts()
        form.instance.day_shift = day_shift
        form.instance.night_shift = night_shift
        form.instance.additional = True
        form.instance.pulse = form.cleaned_data["pulse"]
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.kwargs["pk"]})


class ExaminationsDietListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = Examination
    template_name = "examinations/diets.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return (
            Examination.objects.all()
            .filter(patient=self.patient)
            .exclude(diet__isnull=True)
            .exclude(diet__exact="",)
        )


class ExaminationsFaecesListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = Examination
    template_name = "examinations/faeceses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return (
            Examination.objects.all()
            .filter(patient=self.patient)
            .exclude(faeces__isnull=True)
        )


class ExaminationsPressureListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = Examination
    template_name = "examinations/pressures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return (
            Examination.objects.all()
            .filter(patient=self.patient)
            .exclude(systole__isnull=True)
            .exclude(diastole__isnull=True)
        )


class ExaminationsPulseListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = Examination
    template_name = "examinations/pulses.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return (
            Examination.objects.all()
            .filter(patient=self.patient)
            .exclude(pulse__isnull=True)
        )


class ExaminationsTemperatureListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "examinations"
    model = Examination
    template_name = "examinations/temperatures.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["patient"] = self.patient
        return context

    def get_queryset(self):
        self.patient = Patient.objects.get(pk=self.kwargs["pk"])
        return (
            Examination.objects.all()
            .filter(patient=self.patient)
            .exclude(temperature__isnull=True)
        )


class ExaminationsTemperaturePDFListView(LoginRequiredMixin, generic.ListView):
    model = Examination

    def get_queryset(self):
        return (
            Examination.objects.all()
            .filter(patient=Patient.objects.get(pk=self.kwargs["pk"]))
            .exclude(temperature__isnull=True)
        )

    def render_to_response(self, context, **response_kwargs):
        return self.write_pdf_temperatures_view()

    def write_pdf_temperatures_view(self):
        doc = SimpleDocTemplate("/tmp/kgo-test.pdf")
        styles = getSampleStyleSheet()
        Story = [Spacer(1, 2 * inch)]
        style = styles["Normal"]
        patient = Patient.objects.get(pk=self.kwargs["pk"])

        title = "KARTA GORĄCZKOWA ogólna"
        p = Paragraph(title, style)
        Story.append(p)

        patient_name = patient.name + " " + patient.surname
        p = Paragraph(patient_name, style)
        Story.append(p)

        patient_numbers = (
            "Nr w Książce głównej: "
            + patient.nr_in_main_book
            + ", nr w Książce oddziałowej: "
            + patient.nr_in_ward_book
        )
        p = Paragraph(patient_numbers, style)
        Story.append(p)

        exams = self.get_queryset()
        for exam in exams:
            exam_details = (
                "data: " + " temp. " + str(exam.temperature) + " zmierzona przez "
            )
            p = Paragraph(exam_details, style)
            Story.append(p)

        Story.append(Spacer(1, 0.2 * inch))
        doc.build(Story)

        fs = FileSystemStorage("/tmp")
        with fs.open("kgo-test.pdf") as pdf:
            response = HttpResponse(pdf, content_type="application/pdf")
            response["Content-Disposition"] = 'attachment; filename="kgo-test.pdf"'
            return response

        return response


"""

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

"""
