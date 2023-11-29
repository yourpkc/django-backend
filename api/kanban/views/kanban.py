from rest_framework import viewsets

from api.kanban.models import Kanban
from api.kanban.serializers import KanbanSerializer


class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer
    permission_classes = []
