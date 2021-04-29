from django.urls import path

from polls import views

urlpatterns = [
    path("formss", views.formss, name='formss'),
    path("", views.home, name='home'),
    path("export_formss", views.export_formss, name='export_formss'),
]
