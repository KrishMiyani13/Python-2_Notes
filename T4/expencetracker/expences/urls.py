from django.urls import path
from expences.views import ExpeneViewSet
from rest_framework.routers import DefaultRouter

router  = DefaultRouter()
router.register('expenses',ExpeneViewSet)

urlpatterns = router.urls
