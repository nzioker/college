from rest_framework import serializers
from .models import StudentRegister


class StudentRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = StudentRegister
        fields = '__all__'
