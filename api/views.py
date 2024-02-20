from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import StudentRegister
from .serializers import StudentRegisterSerializer

# Create your views here.

@api_view(['GET'])
def all_students(request):
    # query all the students
    all_students = StudentRegister.objects.all()
    student_serializer = StudentRegisterSerializer(all_students, many=True)
    return Response(student_serializer.data)


@api_view(['GET'])
def student(request, pk):
    # query one student using the id
    student = StudentRegister.objects.get(id=pk)
    student_serializer = StudentRegisterSerializer(student, many=False)
    return Response(student_serializer.data)
    
@api_view(['POST'])
def add_student(request):
    student = StudentRegisterSerializer(data=request.data)
    if student.is_valid():
        student.save()
    
    return Response(student.data)

