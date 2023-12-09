from django.db import transaction
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError


from api.kanban.models import Card
from api.kanban.serializers import CardSerializer


class ColumnViewSet(viewsets.ModelViewSet):
    queryset = Card.objects.all()
    serializer_class = CardSerializer
    permission_classes = []

    @transaction.atomic
    @action(methods=['PATCH'], detail=True)
    def move(self, request, *args, **kwargs):
        card = self.get_object()
        move_to = request.data.get('move_to', 0)
        if move_to is not None:
            move_to = int(move_to)
            if not move_to:
                raise ValidationError({"message": "Field was required: move_to"})
                                     
            if card.pk == move_to:
                raise ValidationError({"message": "Card can't me circle."})
        
        move_to_card = None
        if move_to is not None:
            move_to_card = Card.objects.filter(id=move_to).last()
            if not move_to_card:
                raise ValidationError({"message": f"Not found card pk {move_to}."})

        if card.head == move_to_card:
            raise ValidationError({"message": "Card doesn't move."})
        
        Card.objects.filter(head=card).update(head=card.head)
        Card.objects.filter(head=move_to_card).update(head=card)

        if card.is_tail and card.head:
            card.head.is_tail = True
            card.head.save()

        card.head = move_to_card 
        if move_to_card:
            if move_to_card.is_tail:
                card.is_tail = True
            if card.column != move_to_card.column:
                card.column = move_to_card.column
        card.save()

        if move_to_card and card.is_tail:
            move_to_card.is_tail = False
            move_to_card.save()

        serializer = self.get_serializer(card)
        return Response(serializer.data)
