from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import StudentSerializer
from .models import Student
from rest_framework.response import Response
from django.http import Http404
from rest_framework import status


class StudentCrud(APIView):
    def get(self,request,format = None):
        student = Student.objects.all()
        serializer = StudentSerializer(student,many = True)
        return Response(serializer.data)

    def post(self,request,format = None):
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

class StudentDetail(APIView):
    def get_data(self,pk):
        try:
            return Student.objects.get(pk=pk)
        except Student.DoesNotExist:
            raise Http404    
    def get(self,request,pk,*args,**kwargs):
        std=self.get_data(pk)
        serializer=StudentSerializer(std)
        return Response(serializer.data,status=status.HTTP_200_OK)
    def delete(self,request,pk,*args,**kwargs):
        std=self.get_data(pk)
        std.delete()
        return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self,request,pk,*args,**kwargs):
        std = self.get_data(pk)
        serializer = StudentSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)