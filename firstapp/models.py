from django.db import models
from django.utils.timezone import now

class Destination(models.Model):
    title = models.CharField(max_length=128)
    description=models.TextField()
    image_url=models.URLField( blank=True, null=True)

    def __str__(self):
        return self.title


# Create your models here.
class News(models.Model):
    title = models.CharField(max_length=128)
    description=models.TextField()
    image_url=models.URLField( blank=True, null=True)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title