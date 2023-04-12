from django.db import models

class Click(models.Model):
    count = models.IntegerField(default=0)
