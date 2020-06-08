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
    path(
        "historical/diet/<int:pk>",
        view=views.DietRecommendationHistoricalListView.as_view(),
        name="historical-diet",
    ),
    path(
        "historical/faeces/<int:pk>",
        view=views.FaecesExaminationHistoricalListView.as_view(),
        name="historical-faeces",
    ),
    path(
        "historical/pulse/<int:pk>",
        view=views.PulseExaminationHistoricalListView.as_view(),
        name="historical-pulse",
    ),
    path(
        "historical/pressure/<int:pk>",
        view=views.PressureExaminationHistoricalListView.as_view(),
        name="historical-pressure",
    ),
    path(
        "historical/temperature/<int:pk>",
        view=views.TemperatureExaminationHistoricalListView.as_view(),
        name="historical-temperature",
    ),
]
