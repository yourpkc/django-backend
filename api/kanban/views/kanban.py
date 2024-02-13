from rest_framework import viewsets

from api.kanban.models import Kanban
from api.kanban.serializers import KanbanSerializer, KanbanRepresentSerializer


class KanbanViewSet(viewsets.ModelViewSet):
    queryset = Kanban.objects.all()
    serializer_class = KanbanSerializer
    permission_classes = []

    def get_serializer_class(self, *args, **kwargs):
        if self.action == 'retrieve':
            return KanbanRepresentSerializer

        return super().get_serializer_class(*args, **kwargs)
