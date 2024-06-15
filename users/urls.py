from rest_framework import routers
from .api import UserViewSet, FavoritoViewSet

router = routers.DefaultRouter()

router.register('api/users', UserViewSet, 'users')
router.register('api/favoritos', FavoritoViewSet, 'favoritos')

urlpatterns = router.urls