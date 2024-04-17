import uuid
from django.db import models

# Create your models here.

class Flan(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField()
    is_private = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}: {self.name}'