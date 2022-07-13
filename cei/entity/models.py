import datetime
import uuid

import pytz
from django.db import models


def now():
    return datetime.datetime.now(tz=pytz.UTC)


class Entity(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(editable=False, default=now)
