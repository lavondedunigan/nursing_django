from django.db import models

# Create your models here.
class PatientAccount(models.Model):
    first_name = models.CharField(max_length=70)
    last_name =  models.CharField(max_length=70)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)
    primary_doctor =  models.CharField(max_length=120)
    last_visit = models.DateTimeField()
    number_of_visits = models.DecimalField(max_digits=5, decimal_places=0, null=True, blank=True)
    balance = models.DecimalField(max_digits=12, decimal_places=2)

    def __str__(self):
        return self.first_name + " " + self.last_name
    
    
class PatientBalance(models.Model):
    first_name = models.CharField(max_length=70)
    last_name =  models.CharField(max_length=70)
    phone_number = models.CharField(max_length=20)
    primary =  models.CharField(max_length=120)
    last_visit = models.DateTimeField()
    next_visit = models.DateTimeField()
    previous_balance = models.DecimalField(max_digits=12, decimal_places=2) 
    balance_as_of_today = models.DecimalField(max_digits=12, decimal_places=2)
    
    
class Referrals(models.Model):
    patient_condition = models.CharField(max_length=1000) 
    suitable_specialists = models.CharField(max_length=300)
    communicate_with_patient = models.CharField(max_length=500)
    facilitate_referral_process = models.CharField(max_length=250)
    follow_up = models.CharField(max_length=1000)


    
    
    
    
    
    
    
    
    
    
    
    
    
       