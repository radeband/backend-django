from django.db import models

from _helpers.models import BaseModel


class Facility(BaseModel):
    title = models.CharField(max_length=255)
    essentiality = models.IntegerField()
    category = models.ForeignKey('company.Category', on_delete=models.CASCADE, related_name='facilities')

    class Meta:
        db_table = "facilities"
