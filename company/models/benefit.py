from django.db import models

from _helpers.models import BaseModel



class Benefit(BaseModel):
    title = models.CharField(max_length=255)
    facility = models.ForeignKey('company.Facility', on_delete=models.CASCADE, related_name='benefits')

    class Meta:
        db_table = "benefits"
