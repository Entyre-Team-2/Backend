from rest_framework import serializers
from .models import Entyre

class EntyreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Entyre
        fields = ('id', 'first_name', 'last_name', 'sex', 'dob', 'age', 'weight', 'insurance_comp', 'insurance_num')