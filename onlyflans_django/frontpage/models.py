import uuid
from django.db import models
from django.utils.text import slugify

# Create your models here.

class Flan(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    name = models.CharField(max_length=64)
    description = models.TextField()
    image = models.URLField()
    slug = models.SlugField(max_length=64)
    is_private = models.BooleanField(default=False)

    #Sobreescribo el metodo save para que cada vez que se guarde un objeto se genere un slug
    def save(self, *args, **kwargs):
        
        self.slug = slugify(self.name)

        original_slug = Flan.objects.filter(pk=self.pk).values_list('slug', flat=True).first()
        if self.slug != original_slug:
            count = 1
            while Flan.objects.filter(slug=self.slug).exists():
                self.slug = f"{slugify(self.name)}-{count}"
                count += 1

        super().save(*args, **kwargs)

    @property
    def get_uuid(self):
        return self.uuid

    def __str__(self):
        return f'{self.pk}: {self.name}'
    

class Contact(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    message = models.TextField()
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    @property
    def get_uuid(self):
        return self.uuid

    def __str__(self):
        return f'{self.pk}: {self.name}'