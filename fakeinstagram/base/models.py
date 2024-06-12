from django.db import models
from datetime import datetime
# Create your models here.
class BaseModel(models.Model):
    created_at = models.DateField(auto_now_add=True)
    modified_at = models.DateField(auto_now=True)    

    class Meta:
        abstract = True