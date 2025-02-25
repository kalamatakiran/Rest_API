from django.contrib import admin
from django.urls import path
from .views import hello,ListStudentData,CreateStudentData,RetrieveStudentData,UpdateAPIView,DestroyAPIView,StudentTotalData
from . import views

urlpatterns = [
    path('hello/',views.hello,name='hello'),
    path('ListStudentData/',ListStudentData.as_view()),
    path('CreateStudentData/',CreateStudentData.as_view()),
    path('RetrieveStudentData/',RetrieveStudentData.as_view()),
    path('UpdateAPIView/',UpdateAPIView.as_view()),
    path('DestroyAPIView/',DestroyAPIView.as_view()),
    path('StudentTotalData/',StudentTotalData.as_view()),
    path('StudentTotalData/<int:id>',StudentTotalData.as_view()),
]