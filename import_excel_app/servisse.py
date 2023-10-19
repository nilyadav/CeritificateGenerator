from import_excel_app.models import Excel
from django.shortcuts import redirect
from accredetation_app.models import filter_by_expiry_date
from trainer_app.models import filter_by_trainer_name
def read_data_from_excel(data):
    value = Excel()
    value.ID_No = data[0]
    value.Name_Of_Delegates = data[1]
    value.Certificate_No = data[2]
    value.Course = data[3]
    value.Company = data[4]
    value.Date_Of_issue = data[5]
    value.Date_Of_Expiry = data[6]
    value.Instructor = data[7]
    value.instructor_id = data[8]
    value.accreditaion_id = data[9]
    value.save()
  