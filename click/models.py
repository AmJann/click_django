from django.db import models
import uuid

class Click(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(blank=True,default='count')
    count = models.CharField(max_length=10,default=0)

    def __str__(self):
        return self.title