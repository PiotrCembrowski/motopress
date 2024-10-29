from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    inntro = models.TextField()
    body = models.TextField()
    upload = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now=True)