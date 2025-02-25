from django.shortcuts import render
from rest_framework.response import Response
from django.http import HttpResponse,Http404
from myapp.models import Student
from rest_framework import status
from .serializers import StudentSerializer
from rest_framework.decorators import APIView
from rest_framework.generics import CreateAPIView,UpdateAPIView,RetrieveAPIView,DestroyAPIView,ListAPIView

def hello(request):
    s1='<h1>helloworld</h1>'
    return HttpResponse(s1)

class ListStudentData(ListAPIView):
    queryset=Student.objects.all()
    serializer=StudentSerializer
class CreateStudentData(CreateAPIView):
    queryset=Student.objects.all()
    serializer=StudentSerializer
class UpdateStudentData(UpdateAPIView):
    queryset=Student.objects.all()
    serializer=StudentSerializer
class RetrieveStudentData(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer=StudentSerializer
class DestroyStudentData(DestroyAPIView):
    queryset=Student.objects.all()
    serializer=StudentSerializer

class StudentTotalData(APIView):
    def get(self,request,id=None):
        if id:
            try:
                std_class=Student.objects.get(id=id)
                serializer_class=StudentSerializer(std_class)
                return Response(serializer_class.data,status=status.HTTP_200_OK)
            except Student.DoesNotExist:
                raise Http404
        else:
            std_class=Student.objects.all()
            serializer_class=StudentSerializer(std_class,many=True)
            return Response(serializer_class.data,status=status.HTTP_200_OK)
    def post(self,request):
        serializer_class=StudentSerializer(data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
    def put(self,request,id):
        try:
            std_class=Student.objects.get(id=id)
        except Student.DoesNotExist:
            raise Http404
        serializer_class=StudentSerializer(std_class,data=request.data)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(serializer_class.data,status=status.HTTP_200_OK)
        else:
            return Response(serializer_class.data,status=status.HTTP_201_CREATED)
    def delete(self,request,id):
            try:
                std_class=Student.objects.get(id=id)
            except Student.DoesNotExist:
                raise Http404
            std_class.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
  