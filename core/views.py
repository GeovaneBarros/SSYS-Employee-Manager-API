from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.decorators import api_view, authentication_classes, permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import Employee
from .serializers import EmployeeSerializer
from datetime import date



@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

@api_view()
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def salary_report(request):
    qs = list(Employee.objects.values())
    average =  Employee.objects.aggregate(Avg('salary'))
    
    dictionary = {}
    if len(qs) > 0:
        dictionary['lowest'] = qs[0]
        dictionary['highest'] = qs[0]
        for x in qs:
            if x['salary'] < dictionary['lowest']['salary']:
                dictionary['lowest'] = x
            if x['salary'] > dictionary['highest']['salary']:
                dictionary['highest'] = x
                
        dictionary['average'] =  average['salary__avg']
    
    return Response(dictionary)

@api_view()
@authentication_classes([SessionAuthentication, BasicAuthentication, TokenAuthentication])
@permission_classes([IsAuthenticated])
def age_report(request):
    qs = list(Employee.objects.values())
    dictionary = {}
    
    if len(qs) > 0:
        cont = 0
        sum = 0
        for x in qs:
            sum = sum + calculate_age(x['birth_date'])
            cont = cont + 1
        
        dictionary['younger'] = qs[0]
        dictionary['older'] = qs[0]
        
        for x in qs:
            if x['birth_date'] < dictionary['older']['birth_date']:
                dictionary['older'] = x
            if x['birth_date'] > dictionary['younger']['birth_date']:
                dictionary['younger'] = x

        if cont > 0:
            dictionary['average'] = sum / cont
        else:
            dictionary['average'] = 0

    return Response(dictionary)

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))