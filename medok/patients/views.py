from datetime import date

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse, HttpResponseForbidden
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
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .forms import PatientForm
from .models import Patient
from .utils import check_shift


def write_pdf_view(request):
    doc = SimpleDocTemplate("/tmp/kgo-test.pdf")
    styles = getSampleStyleSheet()
    Story = [Spacer(1, 2 * inch)]
    style = styles["Normal"]
    bogustext = "Testowa strona wydruku KGO"
    p = Paragraph(bogustext, style)
    Story.append(p)
    Story.append(Spacer(1, 0.2 * inch))
    doc.build(Story)

    fs = FileSystemStorage("/tmp")
    with fs.open("kgo-test.pdf") as pdf:
        response = HttpResponse(pdf, content_type="application/pdf")
        response["Content-Disposition"] = 'attachment; filename="kgo-test.pdf"'
        return response

    return response


class PatientCreateView(LoginRequiredMixin, generic.CreateView):
    form_class = PatientForm
    model = Patient
    success_url = reverse_lazy("patients:list")
    template_name = "patients/create.html"


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    context_object_name = "patient"
    model = Patient
    template_name = "patients/detail.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["days"] = self.get_days()
        context["diets"] = self.get_diets()
        context["faeceses"] = self.get_faeceses()
        context["pressures"] = self.get_pressures()
        context["pulses"] = self.get_pulses()
        context["shifts"] = self.get_shifts()
        context["temps"] = self.get_temps()
        return context

    def get_days(self):
        days = list(n for n in range(1, 31))
        return days

    def get_shifts(self):
        shifts = []
        for day in self.get_days():
            shifts.append("R")
            shifts.append("W")
        return shifts

    def get_diets(self):
        results = []
        today = date.today()
        exams = DietRecommendation.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(created__year=today.year)
        exams = exams.filter(created__month=today.month)
        exams = exams.order_by("created")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.created.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.created.day == day:
                    exams_this_day.append(exam)
            if len(exams_this_day) == 2:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.get_diet_display())
                    if exam.night_shift:
                        results.append(exam.get_diet_display())
            elif len(exams_this_day) == 1:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.get_diet_display())
                        results.append("BRAK")
                    if exam.night_shift:
                        results.append("BRAK")
                        results.append(exam.get_diet_display())
            else:
                results.append("BRAK")
                results.append("BRAK")
        return results

    def get_faeceses(self):
        results = []
        today = date.today()
        exams = FaecesExamination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(created__year=today.year)
        exams = exams.filter(created__month=today.month)
        exams = exams.order_by("created")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.created.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.created.day == day:
                    exams_this_day.append(exam)
            if len(exams_this_day) == 2:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.faeces)
                    if exam.night_shift:
                        results.append(exam.faeces)
            elif len(exams_this_day) == 1:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.faeces)
                        results.append("BRAK")
                    if exam.night_shift:
                        results.append("BRAK")
                        results.append(exam.faeces)
            else:
                results.append("BRAK")
                results.append("BRAK")
        return results

    def get_pressures(self):
        results = []
        today = date.today()
        exams = PressureExamination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(created__year=today.year)
        exams = exams.filter(created__month=today.month)
        exams = exams.order_by("created")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.created.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.created.day == day:
                    exams_this_day.append(exam)
            if len(exams_this_day) == 2:
                for exam in exams_this_day:
                    pressure = str(exam.systole) + "/" + str(exam.diastole)
                    if exam.day_shift:
                        results.append(pressure)
                    if exam.night_shift:
                        results.append(pressure)
            elif len(exams_this_day) == 1:
                for exam in exams_this_day:
                    pressure = str(exam.systole) + "/" + str(exam.diastole)
                    if exam.day_shift:
                        results.append(pressure)
                        results.append("BRAK")
                    if exam.night_shift:
                        results.append("BRAK")
                        results.append(pressure)
            else:
                results.append("BRAK")
                results.append("BRAK")
        return results

    def get_pulses(self):
        results = []
        today = date.today()
        exams = PulseExamination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(created__year=today.year)
        exams = exams.filter(created__month=today.month)
        exams = exams.order_by("created")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.created.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.created.day == day:
                    exams_this_day.append(exam)
            if len(exams_this_day) == 2:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.pulse)
                    if exam.night_shift:
                        results.append(exam.pulse)
            elif len(exams_this_day) == 1:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.pulse)
                        results.append("BRAK")
                    if exam.night_shift:
                        results.append("BRAK")
                        results.append(exam.pulse)
            else:
                results.append("BRAK")
                results.append("BRAK")
        return results

    def get_temps(self):
        results = []
        today = date.today()
        exams = TemperatureExamination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(created__year=today.year)
        exams = exams.filter(created__month=today.month)
        exams = exams.order_by("created")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.created.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.created.day == day:
                    exams_this_day.append(exam)
            if len(exams_this_day) == 2:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.temperature)
                    if exam.night_shift:
                        results.append(exam.temperature)
            elif len(exams_this_day) == 1:
                for exam in exams_this_day:
                    if exam.day_shift:
                        results.append(exam.temperature)
                        results.append("BRAK")
                    if exam.night_shift:
                        results.append("BRAK")
                        results.append(exam.temperature)
            else:
                results.append("BRAK")
                results.append("BRAK")
        return results


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
                print("---- night")
                night_shift = True
                day_shift = False
            else:
                print("---- day")
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
