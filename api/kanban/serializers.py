from rest_framework import serializers
from api.kanban.models import Kanban, Column, Card


class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = '__all__'


class KanbanRepresentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Kanban
        fields = '__all__'
    
    def to_representation(self, kanban):
        data = super().to_representation(kanban)
        data['columns'] = ColumnRepresentSerializer(kanban.kanban_columns.all(), many=True).data
        return data

class ColumnRepresentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Column
        fields = '__all__'
    
    def to_representation(self, column):
        data = super().to_representation(column)
        data['cards'] = CardSerializer(column.column_cards, many=True).data
        return data



class ColumnSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not self.instance:
            data['is_tail'] = True
            kanban = data['kanban']
            tail_column = kanban.kanban_columns.filter(is_tail=True).last()
            if tail_column:
                data['head'] = tail_column
        else:
            data.pop('kanban', None)
        return data
    
    def create(self, validated_data):
        column = super().create(validated_data)
        if head_column:= column.head:
            head_column.is_tail = False
            head_column.save()

        return column

    class Meta:
        model = Column
        fields = '__all__'
        read_only_fields = ('is_tail', 'head')

class CardSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not self.instance:
            data['is_tail'] = True
            column = data['column']
            tail_cards = column.column_cards.filter(is_tail=True).last()
            if tail_cards:
                data['head'] = tail_cards
        else:
            data.pop('column', None)
        
        return data    
    
    def create(self, validated_data):
        card = super().create(validated_data)
        if head_card:= card.head:
            head_card.is_tail = False
            head_card.save()
        return card
    
    
    class Meta:
        model = Card
        fields = '__all__'
        read_only_fields = ('is_tail', 'head')
