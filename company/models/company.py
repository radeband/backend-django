from django.db import models

from _helpers.models import BaseModel


class Company(BaseModel):
    name = models.CharField(max_length=255)
    website = models.CharField(max_length=255, null=True, blank=True)
    longitude = models.CharField(max_length=255, null=True, blank=True)
    latitude = models.CharField(max_length=255, null=True, blank=True)
    address = models.CharField(max_length=512, null=True, blank=True)
    logo = models.ImageField(null=True, blank=True, upload_to='companies/logo')
    benefits = models.ManyToManyField(to='company.Benefit', through='company.CompanyBenefit', related_name='companies')

    class Meta:
        db_table = "companies"
