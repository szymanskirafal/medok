from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    path("", view=views.PatientsListView.as_view(), name="patients"),
    path("create/", view=views.PatientCreateView.as_view(), name="create"),
    path("<int:pk>/", view=views.PatientDetailView.as_view(), name="detail"),
    path("<int:pk>/chart/", view=views.PatientChartDetailView.as_view(), name="chart",),
    path(
        "<int:pk>/chart-time-data/",
        view=views.PatientsChartTimeDataDetailView.as_view(),
        name="chart-time-data",
    ),
]
