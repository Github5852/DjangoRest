from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from api.customauth import CustomAuthentication
from rest_framework.permissions import IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
  queryset = Student.objects.all()
  serializer_class = StudentSerializer
  authentication_classes=[TokenAuthentication]
  permission_classes=[IsAuthenticated]
