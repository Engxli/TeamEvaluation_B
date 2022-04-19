from rest_framework.viewsets import ModelViewSet
from .models import Project
from .serializers import ProjectViewSerializer
# Create your views here.

class ProjectViewSet(ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectViewSerializer
