from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from .serializers import PatientSerializer, DiagnosisSerializer, DrugsSerializer
from .models import Patient, Diagnosis, Drugs, Results, Interactions
from rest_framework import status
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist

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
		if request.method == 'POST':
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




class DiagnosisView(APIView):

	def get(self,request):
		if request.method == 'GET':
			resp = []
			for patient in Patient.objects.all():
				temp = {}
				temp['firstname'] = patient.first_name
				temp['lastname'] = patient.last_name
				try:
					temp_result = Results.objects.get(ofPatient = patient)
				except ObjectDoesNotExist:
					temp_result = None
				if temp_result != None:
					temp['riskScore'] = temp_result.risk_score
					temp_interactions= []
					try:
						temp_int = Interactions.objects.filter(ofResult = temp_result)
					except ObjectDoesNotExist:
						temp_int = None
					if temp_int != None:
						for interaction in Interactions.objects.filter(ofResult = temp_result):
							drug_interactions = {}
							drug_interactions['drug1'] = interaction.drug1
							drug_interactions['drug2'] = interaction.drug2
							drug_interactions['riskLevel'] = interaction.risk_level
							temp_interactions.append(drug_interactions)
						temp['interactions'] = temp_interactions
				resp.append(temp)

			return Response(resp)



class DrugsView(viewsets.ModelViewSet):
    serializer_class = DrugsSerializer
    queryset = Drugs.objects.all()