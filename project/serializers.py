
from pyexpat import model

from django.forms import fields
from rest_framework import serializers
from .models import Project
from team.serializers import TeamViewSerializer
from criteria.serializers import CriteriaViewSerializer
class ProjectGetViewSerializer(serializers.ModelSerializer):
    # semester = serializers.
    team = TeamViewSerializer(many=True, read_only=True)
    criteria = CriteriaViewSerializer(many=True)
    class Meta:
        model = Project
        fields = '__all__'


class ProjectViewSerializer(serializers.ModelSerializer):
    # semester = serializers.
    team = TeamViewSerializer(many=True, read_only=True)
    class Meta:
        model = Project
        fields = '__all__'




