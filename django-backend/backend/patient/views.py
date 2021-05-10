from django.shortcuts import render
from rest_framework import viewsets
from .serializers import PatientSerializer, DiagnosisSerializer, DrugsSerializer
from .models import Patient, Diagnosis, Drugs

# Create your views here.

class PatientView(viewsets.ModelViewSet):
    serializer_class = PatientSerializer
    queryset = Patient.objects.all()

class DiagnosisView(viewsets.ModelViewSet):
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()

class DrugsView(viewsets.ModelViewSet):
    serializer_class = DrugsSerializer
    queryset = Drugs.objects.all()