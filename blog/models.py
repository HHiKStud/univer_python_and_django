from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class BlogPost(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Publishing date")
    image = models.ImageField(upload_to = 'images/', verbose_name="Image")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="author", null=True, blank=True)
