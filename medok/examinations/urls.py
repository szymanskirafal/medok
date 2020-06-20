from django.urls import path

from . import views

app_name = "examinations"

urlpatterns = [
    path("create/<int:pk>", view=views.ExaminationCreateView.as_view(), name="create",),
    path(
        "create/<int:pk>additional",
        view=views.ExaminationAdditionalCreateView.as_view(),
        name="create-additional",
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
        "historical/temperature/<int:pk>",
        view=views.ExaminationsTemperatureListView.as_view(),
        name="temperatures",
    ),
]
