from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectViewSerializer,ProjectGetViewSerializer
from rest_framework import permissions
# Create your views here.

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()

    def get_serializer_class(self):
        if(self.request.method in permissions.SAFE_METHODS):
            return ProjectGetViewSerializer
        return ProjectViewSerializer

