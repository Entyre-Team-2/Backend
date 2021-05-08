from django.shortcuts import render
from rest_framework import viewsets
from .serializers import EntyreSerializer
from .models import Entyre

# Create your views here.

class EntyreView(viewsets.ModelViewSet):
    serializer_class = EntyreSerializer
    queryset = Entyre.objects.all()
