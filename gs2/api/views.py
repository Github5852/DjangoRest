import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from .serializers import StudentSerializers
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
@csrf_exempt
def student_create(requests):
    if requests.method == 'POST':
        json_data = requests.body
        stream = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream)
        serializer = StudentSerializers(data =python_data)
        if serializer.is_valid():
            serializer.save()
            response = {'msg': 'data_created'}
            json_data = JSONRenderer().render(response)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONRenderer().render(serializer.errors)
        return HttpResponse(json_data,content_type='application/json')

