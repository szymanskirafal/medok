from django.contrib import admin

from .models import Examination


@admin.register(Examination)
class ExaminationAdmin(admin.ModelAdmin):
    fields = (
        "made",
        "made_by",
        "patient",
        "day_shift",
        "night_shift",
        "additional",
        "temperature",
        "pulse",
        "systole",
        "diastole",
        "diet",
        "faeces",
    )
