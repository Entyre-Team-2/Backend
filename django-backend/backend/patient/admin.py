from django.contrib import admin
from .models import Patient, Diagnosis, Drugs

class PatientAdmin(admin.ModelAdmin):
    pass

class DiagnosisAdmin(admin.ModelAdmin):
	pass

class DrugsAdmin(admin.ModelAdmin):
	pass