from django.db import models

# Create your models here.
class InductionQuizzes(models.Model):
    name        = models.CharField("Name", max_length=30, unique=True)
    publish     = models.BooleanField(null=True)
    data        = models.JSONField()