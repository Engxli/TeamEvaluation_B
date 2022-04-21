
from rest_framework import serializers
from .models import Semester
from project.serializers import ProjectGetViewSerializer
from api.serializers import ModifyDjoserUserSerializer



class SemesterViewSerializer(serializers.ModelSerializer):
    added_by = serializers.RelatedField(source='user',read_only=True)
    project = ProjectGetViewSerializer(many=True, read_only=True)
    class Meta:
        model = Semester
        fields = '__all__'

    def create(self, validated_data):
        validated_data['added_by'] = self.context['user']
        return super().create(validated_data)

class SemesterViewGetSerializer(serializers.ModelSerializer):
    added_by = ModifyDjoserUserSerializer()
    project = ProjectGetViewSerializer(many=True, read_only=True)
    class Meta:
        model = Semester
        fields = '__all__'

