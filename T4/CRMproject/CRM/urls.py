from rest_framework.routers import DefaultRouter
from CRM.views import CustomerViewset,NormalCustomerViewset

router = DefaultRouter()
router.register('IsAdminUser',CustomerViewset,basename='IsAdminUser')
router.register('IsAdminOrReadonly',NormalCustomerViewset,basename='IsAdminOrReadonly')

urlpatterns = router.urls
