from .viewsets import ItemViewSet
from item_view.models import Item
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('Item', ItemViewSet, basename='Item')
