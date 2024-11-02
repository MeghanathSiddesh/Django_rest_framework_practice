from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from apiview.models import Student
from apiview.serializers import StudentSerializer
from rest_framework import status
# Create your models here.
# @api_view(['GET']) here we dont need to specify GET in apiview decorator by default drf provides GET method
# but if there are other methods like post,put,patch,delete in the apiview decorator then if the requsting app sendis get method then it is mandatory to specofy 'GET' in apiview decorator other wise it will send mag like {'detail': 'Method "GET" not allowed.'}
'''@api_view(['GET','POST'])
# if we dont mention the method inside the apiview decorator then it wont throw error and stops the flow of execution insted it will resond as {'detail': 'Method "POST" not allowed.'} also if content type i not mentioned i.e.. media type then it will show some message to sending application that {'detail': 'Unsupported media type "text/plain" in request.'}
def hello_world(request):
    if request.method=='GET':
        print(request.data)
        return Response({'msg':'Hello World'})
    if request.method=='POST':
        print(request.data)
        return Response({'msg':'Data Received','data':request.data})'''
'''@api_view(['GET','POST','PUT','DELETE'])
def Stuent_api(request,pk=None):
    if request.method=='GET':
        id=request.data.get('id')
        # here we will get directly parsered data in request.data ie.. in form of dictionary
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            # here response will convert serialied data into json or other format the client is expecting by content-negotiation
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        # returns whole queryset
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'})
        return Response(serializer.errors)
    if request.method=='PUT':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    if request.method=='DELETE':
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data deleted'})'''
# here you can enter id of the data while entering url in the browser for browsable api for performingoperations on that data ex:http://127.0.0.1:8000/4
@api_view(['GET','POST','PUT','DELETE'])
def Stuent_api(request,pk=None):
    if request.method=='GET':
        id=pk
        # here we will get directly parsered data in request.data ie.. in form of dictionary
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            # here response will convert serialied data into json or other format the client is expecting by content-negotiation
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        # returns whole queryset
        return Response(serializer.data)
    if request.method=='POST':
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Created'},status=status.HTTP_201_CREATED)
        return Response(serializer.errors)
    if request.method=='PUT':
        id=pk
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data Updated'})
        return Response(serializer.errors)
    if request.method=='DELETE':
        id=pk
        stu=Student.objects.get(id=id)
        stu.delete()
        return Response({'msg':'Data deleted'})