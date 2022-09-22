from django.db import models

# Create your models here.


class Page(models.Model):
    path = models.CharField(max_length=200, unique=True)
    title = models.CharField(max_length=200)
    keywords = models.CharField(max_length=500)
    description = models.TextField()

    def __str__(self):
        return self.title
