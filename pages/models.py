from django.db import models

# Create your models here.
class PatientAccount(models.Model):
    first_name = models.CharField(max_length=70)
    last_name =  models.CharField(max_length=70)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    primary =  models.CharField(max_length=120)
    last_visit = models.DateTimeField()
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.last_name