from rest_framework import routers
from .api import *
router = routers.DefaultRouter()

router.register('api/projects', ProjectViewSet, 'projects') 

urlpatterns = router.urls