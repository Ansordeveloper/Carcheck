
from rest_framework import routers

from apps.cars.views import CarAPIViewSet, SpecialMarksAPIViewSet, PeriodsOnwershipAPIViewSet, CarPostAPIViewSet, CarPostCommentAPIViewSet,CarPostFavoriteAPIViewSet,CarPostImageAPIViewSet

router = routers.DefaultRouter()

router.register('cars', CarAPIViewSet, "api_cars")
router.register('special', SpecialMarksAPIViewSet, "api_special_marks")
router.register('periods', PeriodsOnwershipAPIViewSet, "api_periods_onwership")
router.register('posts', CarPostAPIViewSet, 'api_post')
router.register('image', CarPostImageAPIViewSet, "api_posts_image")
router.register('comment', CarPostCommentAPIViewSet, "api_posts_comment")
router.register('favorite', CarPostFavoriteAPIViewSet, "api_posts_favotite")

urlpatterns = router.urls