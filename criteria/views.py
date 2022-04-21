from rest_framework.viewsets import ModelViewSet
from .models import Criteria
from .serializers import CriteriaViewSerializer
# Create your views here.
class CriteriaViewSet(ModelViewSet):
    queryset = Criteria.objects.all()
    serializer_class = CriteriaViewSerializer