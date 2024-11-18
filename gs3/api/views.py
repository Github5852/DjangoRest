import io
from rest_framework.parsers import JSONParser
from .models import Student
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse , JsonResponse
from django.views.decorators.csrf import csrf_exempt

from django.shortcuts import render

# Create your views here.
@csrf_exempt
def student_api(request):
    if request.method == 'GET':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        if id is not None:
            stu = Student.objects.get(id=id)
            serializers = StudentSerializers(stu)
            json_data = JSONRenderer().render(serializers.data)
            return HttpResponse(json_data, content_type='application/json')
        stu = Student.objects.all()
        serializer = StudentSerializers(stu,many=True)
        json_data = JSONRenderer().render(serializer.data)
        return HttpResponse(json_data,content_type='application/json')

    if request.method == 'POST':
        json_data = request.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data = python_data)
        if serializer.is_valid():
            serializer.save()
            res = {'msg' : 'data created'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'PUT':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythond_data = JSONParser().parse(stream)
        id = pythond_data.get("id")
        stu = Student.objects.get(id = id)
        serializer = StudentSerializers(stu, data = pythond_data,partial = True)
        if serializer.is_valid():
            serializer.save()
            res = {"msg" : 'data Updated !!'}
            json_data = JSONRenderer().render(res)
            return HttpResponse(json_data,content_type="application/json")
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data, content_type='application/json')

    if request.method == 'DELETE':
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythond_data = JSONParser().parse(stream)
        id = pythond_data.get("id")
        stu = Student.objects.get(id = id)
        stu.delete()
        res = {"msg" : 'data Deleted !!'}
        # json_data = JSONRenderer().render(res)
        # return HttpResponse(json_data,content_type="application/json")
        return JsonResponse(res, safe=False)




