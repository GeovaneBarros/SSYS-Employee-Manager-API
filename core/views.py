from django.db.models import Avg
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import SessionAuthentication, BasicAuthentication, TokenAuthentication
from .models import Employee
from .serializers import EmployeeSerializer
from datetime import date
from statistics import mean
from rest_framework.views import APIView

class EmployeeViewSet(viewsets.ModelViewSet):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

class salary_report(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self, request):
        qs = list(Employee.objects.all().order_by('salary').values())
        metrics = Employee.objects.aggregate(Avg('salary'))

        response = {
            'lowests': get_start_elem(qs, 'salary'),
            'highests': get_end_elem(qs, 'salary'),
            'average':metrics['salary__avg']
        }
        return Response(response)



class age_report(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication, TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        qs = list(Employee.objects.all().order_by('birth_date').values())
        ages = [calculate_age(x['birth_date']) for x in qs]

        response = {
            'oldests': get_start_elem(qs, 'birth_date'),
            'youngests': get_end_elem(qs, 'birth_date'),
            'average':mean(ages)
        }
        return Response(response)

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def get_start_elem(ordered_elements:list, key_attribute:str):
    '''
        This function gets the first elements of the sorted list. 
        Creates a list because there can be more than one element with minimum value
        ------------------------
        Parameters:
        Sorted list and a dict key for filtering
        -----------------------
        Return:
        List of first elements filtering for key
    '''
    starts = []
    first_elem = ordered_elements[0][key_attribute]
    for elem in ordered_elements:
        if elem[key_attribute] == first_elem:
            starts.append(elem)

    return starts

def get_end_elem(ordered_elements:list, key_attribute:str):
    '''
        This function gets the lasts elements of the sorted list. 
        Creates a list because there can be more than one element with maximun value
        ------------------------
        Parameters:
        Sorted list and a dict key for filtering
        -----------------------
        Return:
        List of last elements filtering for key
    '''
    lasts = []
    last_elem = ordered_elements[-1][key_attribute]
    for i in range(1,len(ordered_elements)):
        if ordered_elements[-i][key_attribute] == last_elem:
            lasts.append(ordered_elements[-i])
    
    return lasts