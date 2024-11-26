from django.urls import path
from . import views

urlpatterns = [
    path("", views.pension_age_calculator, name="pension_age_calculator"),
]
