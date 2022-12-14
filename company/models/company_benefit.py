from django.db import models

from _helpers.models import BaseModel


class CompanyBenefit(BaseModel):
    company = models.ForeignKey('company.Company', on_delete=models.CASCADE, related_name="company_benefits")
    benefit = models.ForeignKey('company.Benefit', on_delete=models.CASCADE, related_name="benefits")
    description = models.TextField(max_length=1024, null=True, blank=True)

    class Meta:
        db_table = "company_benefits"
