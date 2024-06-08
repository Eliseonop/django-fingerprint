from rest_framework.routers import DefaultRouter

from .views import FingerPrintView

router = DefaultRouter()

# router.register('personas', PersonaControllers)

router.register('fingerprint', FingerPrintView)

urlpatterns = router.urls
