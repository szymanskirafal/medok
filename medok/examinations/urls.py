from django.urls import path

from . import views

app_name = "examinations"
urlpatterns = [
    path(
        "additional/faeces/<int:pk>",
        view=views.FaecesExaminationCreateView.as_view(),
        name="additional-faeces",
    ),
    path(
        "additional/pressure/<int:pk>",
        view=views.PressureExaminationCreateView.as_view(),
        name="additional-pressure",
    ),
    path(
        "additional/pulse/<int:pk>",
        view=views.PulseExaminationCreateView.as_view(),
        name="additional-pulse",
    ),
    path(
        "additional/temperature/<int:pk>",
        view=views.TemperatureExaminationCreateView.as_view(),
        name="additional-temperature",
    ),
]
