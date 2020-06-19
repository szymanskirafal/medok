from django.urls import path

from . import views

app_name = "examinations"

urlpatterns = [
    path("create/<int:pk>", view=views.ExaminationCreateView.as_view(), name="create",),
    path(
        "historiacal/diets/<int:pk>",
        view=views.ExaminationsDietListView.as_view(),
        name="diets",
    ),
    path(
        "historiacal/faeceses/<int:pk>",
        view=views.ExaminationsFaecesListView.as_view(),
        name="faeceses",
    ),
    path(
        "historiacal/pressures/<int:pk>",
        view=views.ExaminationsPressureListView.as_view(),
        name="pressures",
    ),
    path(
        "historiacal/pulses/<int:pk>",
        view=views.ExaminationsPulseListView.as_view(),
        name="pulses",
    ),
    path(
        "historiacal/temperature/<int:pk>",
        view=views.ExaminationsTemperatureListView.as_view(),
        name="temperatures",
    ),
]
