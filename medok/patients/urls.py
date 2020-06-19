from django.urls import path

from . import views

app_name = "patients"
urlpatterns = [
    path("", view=views.PatientsListView.as_view(), name="patients"),
    path("create/", view=views.PatientCreateView.as_view(), name="create"),
    path("<int:pk>/", view=views.PatientDetailView.as_view(), name="detail"),
    # path(
    #    "<int:pk>/examinations/",
    #    view=views.PatientExaminationsDetailView.as_view(),
    #    name="examinations",
    # ),
    path("pdf/", view=views.write_pdf_view, name="write_pdf_view"),
]
