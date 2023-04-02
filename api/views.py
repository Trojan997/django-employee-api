from django.shortcuts import render
from rest_framework import viewsets
from api.models import *
from api.serializers import *
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.request import Request
# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
    
    @action(detail = True,methods=['get'])
    def employees(self, request, pk=None):
        try:
            company = Company.objects.get(pk=pk)
            emps = Employee.objects.filter(company=company)
            emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
            return Response(emps_serializer.data)
            # print("Get Employee Details of ", pk)
        except Exception as e:
            return Response({
                'message':'Company might not exist..!!'
            })


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
