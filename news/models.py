from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

# Create your models here.
class NewsPost(models.Model):
    title = models.CharField(max_length = 100, verbose_name="Title")
    content = models.TextField(verbose_name="Content")
    date_published = models.DateTimeField(default=timezone.now, verbose_name="Publishing date")
    image = models.ImageField(upload_to = 'images/', verbose_name="Image")
    author = models.ForeignKey(User, on_delete = models.CASCADE, verbose_name="author", null=True, blank=True)

    def __str__(self):
        return str(self.title)
    
    def get_absolute_url(self):
        return reverse("news:news_detail", kwargs={"pk": self.pk})
    