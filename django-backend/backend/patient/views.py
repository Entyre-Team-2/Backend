from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PatientSerializer, DiagnosisSerializer, DrugsSerializer
from .models import Patient, Diagnosis, Drugs, Results, Interactions
from rest_framework import status
from rest_framework.response import Response

import pandas as pd 
import numpy as np 
import math as math
from math import isnan
import json,requests
from itertools import combinations

from .risk import *

# Create your views here.

class PatientView(APIView):


	def post(self, request):
		patient_info = {}
		patient_info = request.data[0]
		diag_info = []
		diag_info = request.data[1]
		newPatient = Patient(first_name = patient_info['firstname'], last_name = patient_info['lastname'], sex = patient_info['sex'], dob = patient_info['dob'], age = patient_info['age'], weight = patient_info['weight'], insurance_comp = patient_info['insuranceCompany'], insurance_num = patient_info['insuranceNumber'])	
		newPatient.save()
		drug_list = []
		print(newPatient.first_name, "DONE")
		for diag in diag_info:
			newDiag = Diagnosis(ofPatient = newPatient, diag_name = diag['name'])	
			newDiag.save()
			print(newDiag.diag_name, "DONE")
			for drug in diag['drugs']:
				Drugs.objects.create(ofDiagnosis = newDiag, drug_name = drug)
				drug_list.append(drug)
				print(drug, "DONE")
		med_combs = list(combinations(drug_list, 2))
		print(med_combs)
		risks= get_risk(med_combs)
		risk_score = aggregate_risk(risks)
		newResults = Results(ofPatient = newPatient, risk_score = risk_score[1])
		newResults.save()
		print(newResults.risk_score)
		num_entries = len(risk_score[0].index)
		for i in range(num_entries):
			newInteractions = Interactions(ofResult = newResults, drug1 = risk_score[0]['Medicine 1'][i], drug2 = risk_score[0]['Medicine 2'][i], risk_level = risk_score[0]['Degree of Risk'][i])
			newInteractions.save()
			print(str(newInteractions.drug1) + " " + str(newInteractions.drug2) + " " + str(newInteractions.risk_level))
		return Response("Success", status = status.HTTP_200_OK)



class DiagnosisView(viewsets.ModelViewSet):
    serializer_class = DiagnosisSerializer
    queryset = Diagnosis.objects.all()

class DrugsView(viewsets.ModelViewSet):
    serializer_class = DrugsSerializer
    queryset = Drugs.objects.all()