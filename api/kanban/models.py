from django.db import models
from api.utils.models import BaseModel


class Kanban(BaseModel):
    title = models.CharField(max_length=50)

class Column(BaseModel):
    title = models.CharField(max_length=50)
    kanban = models.ForeignKey(Kanban, on_delete=models.CASCADE, related_name="kanban_columns")
    head = models.ForeignKey('self', null=True, on_delete=models.RESTRICT)
    is_tail = models.BooleanField(default=False)
