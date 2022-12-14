from rest_framework.viewsets import ModelViewSet

from company.models import Facility
from company.serializers import FacilitySerializer


class FacilityViewSet(ModelViewSet):
    serializer_class = FacilitySerializer
    # TODO: return category_title
    queryset = Facility.objects.all()
