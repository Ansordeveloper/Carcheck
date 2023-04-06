
from rest_framework import routers

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodsOnwershipAPIViewSet

router = routers.DefaultRouter()
router.register('cars', CarAPIViewSet, "api_cars")
router.register('special', SpecialMarksAPIViewSet, "api_special_marks")
router.register('periods', PeriodsOnwershipAPIViewSet, "api_periods_onwership")
urlpatterns = router.urls