from django.db import models
import uuid

class Click(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    title = models.CharField(max_length=100,blank=True,default='count')
    count = models.CharField(max_length=6,default=0)

    def __str__(self):
        return self.title

class Location(models.Model):
    uuid = models.UUIDField(primary_key=True,unique=True, auto_created=True, default=uuid.uuid4)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.city} | {self.state} | {self.country}"
