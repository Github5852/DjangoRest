from django.shortcuts import render
from .serializers import StudentSerializer
from rest_framework.generics import ListAPIView
from .models import Student
from rest_framework.filters import SearchFilter

class StudentList(ListAPIView):
 queryset = Student.objects.all()
 serializer_class = StudentSerializer
 filter_backends = [SearchFilter]
 search_fields = ['city']
 # search_fields = ['name','city']
 # search_fields = ['^name']

