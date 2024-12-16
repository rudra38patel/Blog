from django.db import models
from django.utils import timezone

# Create your models here.

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
    image = models.ImageField(upload_to='blog_images/', null=True,blank=True)


    def __str__(self):
        return self.title
    
    def snippet(self):
        return self.context[:50]
        