from rest_framework.routers import DefaultRouter
from apimovie.views import MovieViewSet

router = DefaultRouter()
router.register("Rating",MovieViewSet,basename='Rating')

urlpatterns = router.urls
