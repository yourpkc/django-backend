from django.db import models
from api.utils.models import BaseModel


class Kanban(BaseModel):
    title = models.CharField(max_length=50)

class Column(BaseModel):
    title = models.CharField(max_length=50)
    kanban = models.ForeignKey(Kanban, blank=False, null=False,
                               on_delete=models.CASCADE,
                               related_name="kanban_columns")
    head = models.ForeignKey('self', null=True, on_delete=models.RESTRICT)
    is_tail = models.BooleanField(default=False)

class Card(BaseModel):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255, blank=True, null=False,
                                   default="")
    column = models.ForeignKey(Column, blank=False, null=False,
                               on_delete=models.CASCADE, 
                               related_name="kanban_columns")
    head = models.ForeignKey('self', null=True, on_delete=models.RESTRICT)
    is_tail = models.BooleanField(default=False)
