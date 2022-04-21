from rest_framework.viewsets import ModelViewSet
from .models import Semester
from .serializers import SemesterViewSerializer, SemesterViewGetSerializer
from rest_framework import permissions
# Create your views here.

class SemesterViewSet(ModelViewSet):

    def get_queryset(self):
        print(self.request.user)
        # return Semester.objects.filter(added_by=self.request.user.id)
        return Semester.objects.all()

    def get_serializer_class(self):
        if(self.request.method in permissions.SAFE_METHODS):
            return SemesterViewGetSerializer
        return SemesterViewSerializer
    def get_serializer_context(self):
        return ({"user":self.request.user})
