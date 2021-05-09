from rest_framework import serializers
from .models import Patient, Diagnosis, Drugs

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ('id', 'first_name', 'last_name', 'sex', 'dob', 'age', 'weight', 'insurance_comp', 'insurance_num')

class DiagnosisSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diagnosis
        fields = ('ofPatient', 'diag_name')

class DrugsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drugs
        fields = ('ofDiagnosis', 'drug_name', 'strength', 'dosage', 'form')
 
