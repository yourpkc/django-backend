from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError

from api.kanban.models import Column
from api.kanban.serializers import ColumnSerializer

class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer
    permission_classes = []


    @transaction.atomic
    @action(methods=['PATCH'], detail=True)
    def move(self, request, *args, **kwargs):
        column = self.get_object()
        move_to = request.data.get('move_to', 0)
        if move_to is not None:
            move_to = int(move_to)
            if not move_to:
                raise ValidationError({"message": "Field was required: move_to"})
                                     
            if column.pk == move_to:
                raise ValidationError({"message": "Column can't me circle."})
        
        move_to_column = None
        if move_to is not None:
            move_to_column = Column.objects.filter(id=move_to).last()
            if not move_to_column:
                raise ValidationError({"message": f"Not found column pk {move_to}."})
            if move_to_column.kanban.pk != column.kanban.pk:
                raise ValidationError({"message": "Can't move to others kanban."})

        if column.head == move_to_column:
            raise ValidationError({"message": "Column doesn't move."})
        
        Column.objects.filter(head=column).update(head=column.head)
        Column.objects.filter(head=move_to_column).update(head=column)

        if column.is_tail and column.head:
            column.head.is_tail = True
            column.head.save()

        column.head = move_to_column 
        if move_to_column and move_to_column.is_tail:
                column.is_tail = True
        column.save()

        if move_to_column and column.is_tail:
            move_to_column.is_tail = False
            move_to_column.save()

        serializer = self.get_serializer(column)
        return Response(serializer.data)

