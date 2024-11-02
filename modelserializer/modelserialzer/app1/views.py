from django.shortcuts import render
from app1.models import StudentModel
from app1.serializers import StudentSerializer
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework.views import APIView
# Create your views here.
@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        try:
            if request.body:
                json_data=request.body
                print(json_data)
                stream=io.BytesIO(json_data)
                python_data=JSONParser().parse(stream)
                id=python_data.get('id',None)
                print(id)
                if id is not None:
                    stu=StudentModel.objects.get(id=id)
                    serializer=StudentSerializer(stu)
                    json_data=JSONRenderer().render(serializer.data)
                    return HttpResponse(json_data)
        except:
            return JsonResponse({'error':'student not found'},status=404)
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        name=python_data.get('name',None)
        if id is not None:
            stu=StudentModel.objects.get(name=name)
            serializer=StudentSerializer(stu,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                msg={'sucess':'yeahss'}
                json_data=JSONRenderer().render(msg)
                return HttpResponse(json_data)
        else:
            return JsonResponse({'error':'student not found'},status=404)