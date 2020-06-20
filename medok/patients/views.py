import calendar

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.utils import timezone
from django.views import generic
from examinations.models import Examination
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer

from .forms import PatientForm
from .models import Patient
from .utils import get_current_shifts


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
    success_url = reverse_lazy("patients:patients")
    template_name = "patients/create.html"


class PatientDetailView(LoginRequiredMixin, generic.DetailView):
    context_object_name = "patient"
    model = Patient
    template_name = "patients/detail.html"

    def check_examination_need(self):
        examinations = Examination.objects.all()
        examinations = examinations.filter(patient=self.get_object(),)
        examinations = examinations.filter(made_on__date=timezone.now().date(),)
        examinations = examinations.filter(additional=False)
        day_shift, night_shift = get_current_shifts()
        examinations = examinations.filter(day_shift=day_shift)
        examinations = examinations.filter(night_shift=night_shift)
        if examinations.exists():
            return False
        else:
            return True

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["days"] = self.get_days()
        context["diets"] = self.get_diets()
        context["examination_has_to_be_made"] = self.check_examination_need()
        context["faeceses"] = self.get_faeceses()
        context["pressures"] = self.get_pressures()
        context["pulses"] = self.get_pulses()
        context["shifts"] = self.get_shifts()
        context["temps"] = self.get_temps()
        return context

    def get_days(self):
        days = calendar.monthrange(timezone.now().year, timezone.now().month)[1]
        days = range(1, days + 1)
        return days

    def get_shifts(self):
        shifts = []
        for day in self.get_days():
            shifts.append("R")
            shifts.append("W")
        return shifts

    def get_faeceses(self):
        results = []
        exams = Examination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(made_on__year=timezone.now().year)
        exams = exams.filter(made_on__month=timezone.now().month)
        exams = exams.order_by("made_on")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.made_on.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.made_on.day == day:
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

    def get_diets(self):
        results = []
        exams = Examination.objects.all()
        exams = exams.filter(patient=self.get_object())
        for exam in exams:
            print("-- additional: ", exam.additional)
        exams = exams.filter(additional=False)
        exams = exams.filter(made_on__year=timezone.now().year)
        exams = exams.filter(made_on__month=timezone.now().month)
        exams = exams.order_by("made_on")
        days_exams_was_made = set()
        for exam in exams:
            print("-- addi: ", exam.additional)
            days_exams_was_made.add(exam.made_on.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.made_on.day == day:
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

    def get_pressures(self):
        results = []
        exams = Examination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(made_on__year=timezone.now().year)
        exams = exams.filter(made_on__month=timezone.now().month)
        exams = exams.order_by("made_on")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.made_on.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.made_on.day == day:
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
        exams = Examination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(made_on__year=timezone.now().year)
        exams = exams.filter(made_on__month=timezone.now().month)
        exams = exams.order_by("made_on")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.made_on.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.made_on.day == day:
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
        exams = Examination.objects.all()
        exams = exams.filter(patient=self.get_object())
        exams = exams.filter(additional=False)
        exams = exams.filter(made_on__year=timezone.now().year)
        exams = exams.filter(made_on__month=timezone.now().month)
        exams = exams.order_by("made_on")
        days_exams_was_made = set()
        for exam in exams:
            days_exams_was_made.add(exam.made_on.day)
        for day in self.get_days():
            exams_this_day = []
            for exam in exams:
                if exam.made_on.day == day:
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


"""
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
        faeces_form = self.get_form(form_class=self.faeces_form_class)
        pressure_form = self.get_form(form_class=self.pressure_form_class)
        pulse_form = self.get_form(form_class=self.pulse_form_class)
        temperature_form = self.get_form(form_class=self.temperature_form_class)
        shift = check_shift()

        if shift == "night":
            night_shift = True
            day_shift = False
        else:
            night_shift = False
            day_shift = True

        if diet_form.is_valid():
            if faeces_form.is_valid():
                if pulse_form.is_valid():
                    if pressure_form.is_valid():
                        if temperature_form.is_valid():
                            DietRecommendation.objects.create(
                                made_by=self.request.user,
                                patient=self.object,
                                diet=diet_form.cleaned_data["diet"],
                                day_shift=day_shift,
                                night_shift=night_shift,
                            )
                            FaecesExamination.objects.create(
                                made_by=self.request.user,
                                patient=self.object,
                                faeces=faeces_form.cleaned_data["faeces"],
                                day_shift=day_shift,
                                night_shift=night_shift,
                            )
                            PressureExamination.objects.create(
                                made_by=self.request.user,
                                patient=self.object,
                                systole=pressure_form.cleaned_data["systole"],
                                diastole=pressure_form.cleaned_data["diastole"],
                                day_shift=day_shift,
                                night_shift=night_shift,
                            )
                            PulseExamination.objects.create(
                                made_by=self.request.user,
                                patient=self.object,
                                pulse=pulse_form.cleaned_data["pulse"],
                                day_shift=day_shift,
                                night_shift=night_shift,
                            )
                            TemperatureExamination.objects.create(
                                made_by=self.request.user,
                                patient=self.object,
                                temperature=temperature_form.cleaned_data[
                                    "temperature"
                                ],
                                day_shift=day_shift,
                                night_shift=night_shift,
                            )
                            return self.form_valid(temperature_form)
                        else:
                            return self.form_invalid(temperature_form)
                    else:
                        return self.form_invalid(pressure_form)
                else:
                    return self.form_invalid(pulse_form)
            else:
                return self.form_invalid(faeces_form)
        else:
            return self.form_invalid(diet_form)

    def get_success_url(self):
        return reverse("patients:detail", kwargs={"pk": self.object.pk})
"""


class PatientsListView(LoginRequiredMixin, generic.ListView):
    context_object_name = "patients"
    model = Patient
    template_name = "patients/patients.html"
