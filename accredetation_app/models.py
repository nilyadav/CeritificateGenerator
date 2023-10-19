from django.db import models

# Create your models here.
class Accriditaion(models.Model):
    name_of_accreditation = models.CharField(max_length=100)
    expiry_date = models.DateField()
    accreditation_logo = models.FileField(unique=True,blank=False,null=False,upload_to='shop')

    def __str__(self):
        return self.name_of_accreditation

    class Meta:
        db_table = "Accriditation"

    
def filter_by_expiry_date(expiry):
        return Accriditaion.objects.filter(expiry_date__exact = expiry).first()
