from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField()
    intro = models.TextField()
    body = models.TextField()
    upload = models.ImageField(upload_to='uploads/')
    created_at = models.DateTimeField(auto_now_add=True)
    banner = models.ImageField(default='image.png', blank=True)
    
    def __str__(self):
        return self.title
    
class Image(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    image = models.ImageField()
        