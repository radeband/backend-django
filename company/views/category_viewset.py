from rest_framework.viewsets import ModelViewSet

from company.models import Category
from company.serializers import CategorySerializer


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
