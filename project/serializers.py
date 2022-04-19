
from pyexpat import model

from django.forms import fields
from semester.models import Semester
from rest_framework import serializers
from .models import Project


class ProjectViewSerializer(serializers.ModelSerializer):
    # semester = serializers.
    class Meta:
        model = Project
        fields = '__all__'




