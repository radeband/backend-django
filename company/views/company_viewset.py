from rest_framework.viewsets import ModelViewSet

from company.models import Company
from company.serializers import CompanySerializer


class CompanyViewSet(ModelViewSet):
    serializer_class = CompanySerializer
    queryset = Company.objects.all()
