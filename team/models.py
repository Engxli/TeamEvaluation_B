from django.db import models
from project.models import Project
# Create your models here.


class Team(models.Model):
    name = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='team')
    



