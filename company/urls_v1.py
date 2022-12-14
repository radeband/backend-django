from rest_framework.routers import DefaultRouter

from company.views import (
    CompanyViewSet,
    CategoryViewSet,
    FacilityViewSet
)

router = DefaultRouter()

router.register('companies', CompanyViewSet)
router.register('categories', CategoryViewSet)
router.register('facilities', FacilityViewSet)

urlpatterns = []

urlpatterns += router.urls
