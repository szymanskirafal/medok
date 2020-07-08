from django.urls import path

from . import views

app_name = "examinations"

urlpatterns = [
    path("create/<int:pk>", view=views.ExaminationCreateView.as_view(), name="create",),
    path(
        "create/<int:pk>/additional/diet/",
        view=views.ExaminationAdditionalDietCreateView.as_view(),
        name="create-additional-diet",
    ),
    path(
        "create/<int:pk>/additional/faeces/",
        view=views.ExaminationAdditionalFaecesCreateView.as_view(),
        name="create-additional-faeces",
    ),
    path(
        "create/<int:pk>/additional/pressure/",
        view=views.ExaminationAdditionalPressureCreateView.as_view(),
        name="create-additional-pressure",
    ),
    path(
        "create/<int:pk>/additional/pulse/",
        view=views.ExaminationAdditionalPulseCreateView.as_view(),
        name="create-additional-pulse",
    ),
    path(
        "create/<int:pk>/additional/temperature/",
        view=views.ExaminationAdditionalTemperatureCreateView.as_view(),
        name="create-additional-temperature",
    ),
    path(
        "historical/diets/<int:pk>",
        view=views.ExaminationsDietListView.as_view(),
        name="diets",
    ),
    path(
        "historical/faeceses/<int:pk>",
        view=views.ExaminationsFaecesListView.as_view(),
        name="faeceses",
    ),
    path(
        "historical/pressures/<int:pk>",
        view=views.ExaminationsPressureListView.as_view(),
        name="pressures",
    ),
    path(
        "historical/pulses/<int:pk>",
        view=views.ExaminationsPulseListView.as_view(),
        name="pulses",
    ),
    path(
        "historical/temperatures/<int:pk>",
        view=views.ExaminationsTemperatureListView.as_view(),
        name="temperatures",
    ),
    path("pdf/", view=views.ExaminationsPDFView.as_view(), name="pdf",),
]
