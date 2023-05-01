from app.models import *
from rest_framework import serializers

class EmpForm(serializers.ModelSerializer):
    class Meta:
        model=Emp
        fields='__all__'