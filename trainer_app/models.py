from django.db import models

# Create your models here.
from django.db import models
from .validator import validate_file_extension
class Trainer(models.Model):
    T_name = models.CharField(max_length=20)
    email = models.EmailField(blank=False,null=False,unique=True,)
    optional_email = models.EmailField(blank=True,unique=True,)
    signature = models.FileField(upload_to="shop",default="" ,unique=True,)

    def __str__(self) -> str:
        return self.T_name

    class Meta:
        db_table = "Trainer"

def filter_by_trainer_name(t_name):
    return Trainer.objects.filter(T_name__exact = t_name).first()