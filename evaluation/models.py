from django.db import models
from project.models import Project
import uuid


class Evaluation(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    project = models.OneToOneField(Project, on_delete=models.CASCADE, related_name="evaluation")
    avg = models.JSONField(null=True, blank=True)