from rest_framework.viewsets import ModelViewSet
from .models import Judge
from .serializers import JudgeSerializers,JudgeCreateSerializers
# Create your views here.
class JudgeViewset(ModelViewSet):
    queryset = Judge.objects.all()

    def get_serializer_class(self):
        if(self.request.method == "POST"):
            return JudgeCreateSerializers
        return JudgeSerializers
