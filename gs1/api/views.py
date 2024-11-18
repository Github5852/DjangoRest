from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
# Create your views here.
def student_detail(request,pk):
    stu = Student.objects.get(id=pk)
    serializers = StudentSerializers(stu)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type='application/json')
    #return JsonResponse(serializers.data)

# Queryset - all Data
def student_list(request):
    stu = Student.objects.all()
    serializers = StudentSerializers(stu,many=True)
    json_data = JSONRenderer().render(serializers.data)
    return HttpResponse(json_data,content_type='application/json')
    # return JsonResponse(serializers.data, safe = False)


