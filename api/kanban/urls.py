from rest_framework import routers
from django.urls import path

from api.kanban.views.kanban import KanbanViewSet
from api.kanban.views.column import ColumnViewSet


router = routers.SimpleRouter()
router.register('kanban', KanbanViewSet)
router.register('column', ColumnViewSet)

urlpatterns = router.urls
