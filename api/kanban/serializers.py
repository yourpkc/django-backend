from rest_framework import serializers
from api.kanban.models import Kanban, Column


class KanbanSerializer(serializers.ModelSerializer):
    class Meta:
        model = Kanban
        fields = '__all__'


class ColumnSerializer(serializers.ModelSerializer):

    def to_internal_value(self, data):
        data = super().to_internal_value(data)
        if not self.instance:
            data['is_tail'] = True

            kanban = data['kanban']
            tail_column = kanban.kanban_columns.filter(is_tail=True).last()
            if tail_column:
                data['head'] = tail_column
        
        return data    
    
    class Meta:
        model = Column
        fields = '__all__'
        read_only_fields = ('is_tail', 'head')
