import imp
from rest_framework.viewsets import ModelViewSet
from .models import Evaluation
from .serializers import EvaluationSerializers
from .permissions import LockedProject

# Create your views here.

class EvaluationViewset(ModelViewSet):
    queryset = Evaluation.objects.all()
    serializer_class = EvaluationSerializers
    permission_classes=[LockedProject]
