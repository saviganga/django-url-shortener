from django.db import models
import uuid

# Create your models here.
class URLShortener(models.Model):

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    original_url = models.URLField(max_length=250)
    shortened_url = models.URLField(max_length=30, unique=True)
    shortened_url_code = models.CharField(max_length=20)
    added_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        unique_together = ("original_url", "shortened_url")
        ordering = ["-added_on"]

