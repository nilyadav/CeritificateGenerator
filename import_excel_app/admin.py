from django.contrib import admin

# Register your models here.
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import Excel

@admin.register(Excel)
class ExcelAdmin(ImportExportModelAdmin):
    list_display = ['ID_No','Name_Of_Delegates','Certificate_No','Course','Company','Date_Of_Expiry','Instructor','instructor_id','accreditaion_id']