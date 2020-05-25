from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    path("", view=views.PatientsListView.as_view(), name="list"),
    path("create/", view=views.PatientCreateView.as_view(), name="create"),
    path("<int:pk>/", view=views.PatientDetailView.as_view(), name="detail"),
    path(
        "<int:pk>/examinations/",
        view=views.PatientExaminationsDetailView.as_view(),
        name="examinations",
    ),
]
