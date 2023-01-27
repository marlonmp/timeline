from datetime import datetime
from uuid import uuid4

from django.db import models


class BaseModel(models.Model):

    uuid = models.UUIDField(unique=True, editable=False, default=uuid4)

    created_at = models.DateTimeField(editable=False, default=datetime.now())

    class Meta:
        abstract = True
