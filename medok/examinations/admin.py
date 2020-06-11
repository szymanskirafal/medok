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
    )


@admin.register(FaecesExamination)
class FaecesExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(PressureExamination)
class PressureExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(PulseExamination)
class PulseExaminationAdmin(admin.ModelAdmin):
    pass


@admin.register(TemperatureExamination)
class TemperatureExaminationAdmin(admin.ModelAdmin):
    pass
