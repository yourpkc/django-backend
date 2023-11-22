from django.db import models
from django.contrib.auth.models import User
from safedelete.models import SafeDeleteModel
from safedelete.models import SOFT_DELETE_CASCADE


class BaseModel(SafeDeleteModel):
    _safedelete_policy = SOFT_DELETE_CASCADE
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)
    # created_by = models.ForeignKey(User, on_delete=models.CASCADE, editable=False)
    # updated_by = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        abstract = True