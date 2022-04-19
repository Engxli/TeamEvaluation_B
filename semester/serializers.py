
from dataclasses import field
from rest_framework import serializers
from .models import Semester
from project.serializers import ProjectViewSerializer

class SemesterViewSerializer(serializers.ModelSerializer):
    project = ProjectViewSerializer(many=True, read_only=True)
    class Meta:
        model = Semester
        fields = '__all__'

