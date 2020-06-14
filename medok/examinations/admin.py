from django.contrib import admin

from .models import (
    DietRecommendation,
    FaecesExamination,
    PressureExamination,
    PulseExamination,
    TemperatureExamination,
)


@admin.register(DietRecommendation)
class DietRecommendationAdmin(admin.ModelAdmin):
    fields = (
        "created",
        "made_by",
        "patient",
        "diet",
        "day_shift",
        "night_shift",
        "additional",
    )


@admin.register(FaecesExamination)
class FaecesExaminationAdmin(admin.ModelAdmin):
    fields = (
        "created",
        "made_by",
        "patient",
        "faeces",
        "day_shift",
        "night_shift",
        "additional",
    )


@admin.register(PressureExamination)
class PressureExaminationAdmin(admin.ModelAdmin):
    fields = (
        "created",
        "made_by",
        "patient",
        "systole",
        "diastole",
        "day_shift",
        "night_shift",
        "additional",
    )


@admin.register(PulseExamination)
class PulseExaminationAdmin(admin.ModelAdmin):
    fields = (
        "created",
        "made_by",
        "patient",
        "pulse",
        "day_shift",
        "night_shift",
        "additional",
    )


@admin.register(TemperatureExamination)
class TemperatureExaminationAdmin(admin.ModelAdmin):
    fields = (
        "created",
        "made_by",
        "patient",
        "temperature",
        "day_shift",
        "night_shift",
        "additional",
    )
