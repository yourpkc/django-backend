from rest_framework import viewsets

from api.kanban.models import Column
from api.kanban.serializers import ColumnSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = []
