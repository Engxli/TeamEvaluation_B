
from pyexpat import model

from django.forms import fields
from rest_framework import serializers
from .models import Project
from team.serializers import TeamViewSerializer

class ProjectViewSerializer(serializers.ModelSerializer):
    # semester = serializers.
    team = TeamViewSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'




