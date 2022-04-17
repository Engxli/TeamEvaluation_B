from rest_framework.viewsets import ModelViewSet
from .models import Semester
from .serializers import SemesterViewSerializer
# Create your views here.

class SemesterViewSet(ModelViewSet):
    queryset = Semester.objects.all()
    serializer_class = SemesterViewSerializer
