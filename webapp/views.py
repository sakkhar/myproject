from django.shortcuts import render

# Create your views here.
from rest_framework.response import Response
from rest_framework.views import APIView

from webapp.models import employee
from webapp.serializer import employeeserializer


class employeeList(APIView):

    def get(self, request):
        employee1 = employee.objects.all()
        serializer = employeeserializer(employee1, many=True)
        return Response(serializer.data)



    def post(self):
        pass