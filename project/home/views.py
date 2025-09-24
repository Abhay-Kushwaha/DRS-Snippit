from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from home.models import Person
from home.serializers import *

# Create your views here.
@api_view(['GET'])  
def home(request):
    if request.method == 'GET':
        print(request.GET.get('search'))
        return Response({'message': 'Hello, This is Django Home!\n'})
    
@api_view(['GET','POST','PUT','DELETE','PATCH'])
def employee(request):
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response({'Persons':serializer.data})
    
    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data Saved successfully!', 'data':serializer.data})
        return Response({"Error":serializer.errors}, status=400)
    
    elif request.method == 'PUT':
        data=request.data
        obj=Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(obj, data=data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data Updated successfully!', 'data':serializer.data})
        return Response({"Error":serializer.errors}, status=400)
    
    elif request.method == 'PATCH':             #partially update
        data=request.data
        obj=Person.objects.get(id=data.get('id'))
        serializer = PersonSerializer(obj, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Data Updated successfully!', 'data':serializer.data})
        return Response({"Error":serializer.errors}, status=400)
    
    elif request.method == 'DELETE':
        data=request.data
        obj=Person.objects.get(id=data.get('id'))
        obj.delete()
        return Response({'message': 'Data Deleted successfully!'})