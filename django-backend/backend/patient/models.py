from django.db import models

# Create your models here.

class Patient(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    dob = models.DateField(max_length=8)
    age = models.IntegerField()
    weight = models.IntegerField()
    insurance_comp = models.CharField(max_length=100)
    insurance_num = models.CharField(max_length=15)

    def __str__(self):
        return self.insurance_num

class Diagnosis(models.Model):
    ofPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diag_name = models.CharField(max_length=20)

    def __str__(self):
        return self.diag_name

class Drugs(models.Model):
    ofDiagnosis = models.ForeignKey(Diagnosis, on_delete=models.CASCADE)
    drug_name = models.CharField(max_length=15)

class Results(models.Model):
    ofPatient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    risk_score = models.CharField(max_length = 20)

    def __str__(self):
        return self.risk_score


class Interactions(models.Model):
    ofResult = models.ForeignKey(Results, on_delete=models.CASCADE)
    drug1 = models.CharField(max_length = 20)
    drug2 = models.CharField(max_length = 20)
    risk_level = models.IntegerField()

