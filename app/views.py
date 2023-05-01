from django.shortcuts import render

# Create your views here.

from app.models import *
from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from app.serializers import *
from rest_framework.permissions import IsAuthenticated

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def listemps(request):
    queryset=Emp.objects.all()
    esc=EmpForm(queryset,many=True)
    data=esc.data
    return Response(data)




