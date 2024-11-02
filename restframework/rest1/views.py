from django.shortcuts import render
from django.http import HttpResponse
from rest1.serializers import StudentSerializer
from rest1.models import StudentModels
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.core.serializers.json import DjangoJSONEncoder
from django.http import JsonResponse
import io
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
@method_decorator(csrf_exempt,name='dispatch')
class StudentApi(View):
    def get(self,request,*args,**kwargs):
        # stu=StudentModels.objects.all() this gets all data of studentmodel from database
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id',None)
        if id is not None:
            stu=StudentModels.objects.get(id=id)
            serializer=StudentSerializer(stu)
            json_data=JSONRenderer().render(serializer.data)
            return HttpResponse(json_data)
        stu=StudentModels.objects.all()
        serializer=StudentSerializer(stu,many=True)
        json_data=JSONRenderer().render(serializer.data)
        return HttpResponse(json_data)
    def post(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        serializer=StudentSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            resp={'msg':'date created'}
            return JsonResponse(data=resp,safe=True,encoder=DjangoJSONEncoder,json_dumps_params=None)
        else:
            json_data=JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data)
    def put(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        age=python_data.get('age')
        stu=StudentModels.objects.filter(age=age)
        updated_record=[]
        errors=[]
        for s in stu:
            serializer=StudentSerializer(s,data=python_data,partial=True)
            if serializer.is_valid():
                serializer.save()
                updated_record.append(serializer.data)
            else:
                errors.append(serializer.errors)
        if errors:
            return JsonResponse({'upadetd_date':updated_record,'errors':errors},status=207)
        else:
            return JsonResponse({'msg':'all records updated successfully','updated':updated_record},status=200)
    def delete(self,request,*args,**kwargs):
        json_data=request.body
        stream=io.BytesIO(json_data)
        python_data=JSONParser().parse(stream)
        id=python_data.get('id') 
        stu=StudentModels.objects.get(id=id)
        stu.delete()
        resp={'msg':'data deleted'}
        return JsonResponse(data=resp,safe=True,encoder=DjangoJSONEncoder,json_dumps_params=None)
    














# # Create your views here.
# @csrf_exempt
# def processing(request):
#     if request.method=='POST':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         serializer=StudentSerializer(data=python_data)
#         if serializer.is_valid():
#             serializer.save()
#             resp={'msg':'date created'}
#             return JsonResponse(data=resp,safe=True,encoder=DjangoJSONEncoder,json_dumps_params=None)
#         else:
#             json_data=JSONRenderer().render(serializer.errors)
#             return HttpResponse(json_data)
# @csrf_exempt  
# def update_data(request):
#     if request.method=='PUT':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         age=python_data.get('age')
#         stu=StudentModels.objects.filter(age=age)
#         updated_record=[]
#         errors=[]
#         for s in stu:
#             serializer=StudentSerializer(s,data=python_data,partial=True)
#             if serializer.is_valid():
#                 serializer.save()
#                 updated_record.append(serializer.data)
#             else:
#                 errors.append(serializer.errors)
#         if errors:
#             return JsonResponse({'upadetd_date':updated_record,'errors':errors},status=207)
#         else:
#             return JsonResponse({'msg':'all records updated successfully','updated':updated_record},status=200)
# @csrf_exempt
# def delete_data(request):
#     if request.method=='DELETE':
#         json_data=request.body
#         stream=io.BytesIO(json_data)
#         python_data=JSONParser().parse(stream)
#         id=python_data.get('id')
#         stu=StudentModels.objects.get(id=id)
#         stu.delete()
#         resp={'msg':'data deleted'}
#         return JsonResponse(data=resp,safe=True,encoder=DjangoJSONEncoder,json_dumps_params=None)
#     return JsonResponse({'msg':'errors'})

# @csrf_exempt
# def get_data(request):
#     if request.method=='GET':
#         stu=StudentModels.objects.all()
#         serializer=StudentSerializer(stu,many=True)
#         json_data=JSONRenderer().render(serializer.data)
#         return HttpResponse(json_data)