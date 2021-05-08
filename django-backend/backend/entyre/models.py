from django.db import models

# Create your models here.

class Entyre(models.Model):
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)
    sex = models.CharField(max_length=15)
    dob = models.DateField(max_length=8)
    age = models.IntegerField()
    weight = models.IntegerField()
    insurance_comp = models.TextField()
    insurance_num = models.IntegerField()

    def _str_(self):
        return self.first_name
