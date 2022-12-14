import uuid

from django.db import models

from _helpers.models import BaseModel



class Category(BaseModel):
    title = models.CharField(max_length=255, unique=True)
    description = models.TextField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "categories"
