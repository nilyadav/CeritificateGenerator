from django.urls import path
from . import views

app_name = "accredetation_app"
urlpatterns = [
    path('add_accreditaion/',views.add_accreditation,name="add_accreditaion"),
]
