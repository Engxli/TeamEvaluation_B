from rest_framework.viewsets import ModelViewSet
from .models import Team
from .serializers import TeamViewSerializer
# Create your views here.

class TeamViewSet(ModelViewSet):
    queryset = Team.objects.all()
    serializer_class = TeamViewSerializer
