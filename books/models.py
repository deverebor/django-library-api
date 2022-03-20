from django.db import models
from uuid import uuid4

# Create your models here.

def upload_image_book(instance, filename):
  return f"{instance.id_book}-{filename}"

class Books(models.Model):
  id_book = models.UUIDField(primary_key=True, default=uuid4, editable=False)
  title = models.CharField(max_length=255)
  author = models.CharField(max_length=255)
  release = models.IntegerField()
  book_state = models.CharField(max_length=255)
  pages = models.IntegerField()
  publishing_company = models.CharField(max_length=255)
  create_at = models.DateTimeField(auto_now_add=True)
  image = models.ImageField(upload_to=upload_image_book, blank=True, null=True)