from django.shortcuts import render
from rest_framework import generics, permissions

from backapp.models import Teacher
from backapp.serializer import TeacherSerializer


# Create your views here.
class Teacher_List(generics.ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]


class Teacher_Detail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer
    # permission_classes = [permissions.IsAuthenticated]