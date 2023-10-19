from django.db import models
from trainer_app.models import Trainer
from accredetation_app.models import Accriditaion
# Create your models here.
class Excel(models.Model):
    ID_No = models.CharField(max_length=20) 
    Name_Of_Delegates = models.CharField(max_length=100)
    Certificate_No = models.CharField(max_length=40)
    Course = models.CharField(max_length=40)
    Company = models.CharField(max_length=50)
    Date_Of_issue = models.DateField()
    Date_Of_Expiry = models.DateField()
    Instructor = models.CharField(max_length=40)
    instructor_id = models.ForeignKey(Trainer, on_delete=models.CASCADE,related_name="excel_instructor")
    accreditaion_id = models.ForeignKey(Accriditaion,on_delete=models.CASCADE,related_name="excel_expiry")
    pdf_url = models.TextField(blank=True, null=True)

    def __str__(self) -> str:
        return self.Name_Of_Delegates

    class Meta:
        db_table = "Excel"

