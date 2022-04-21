from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Semester(models.Model):
    name = models.CharField(max_length=255)
    added_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='semester')
