from django.db import models
import uuid

class Click(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    count = models.IntegerField(default=0)

    def __str__(self):
        return self.title