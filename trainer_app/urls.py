from django.urls import path
from . import views
app_name = "trainer_app"   

urlpatterns = [
    path('add_instructor/',views.add_instructor,name="add_instructor"),
]