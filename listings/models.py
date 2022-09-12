from django.db import models

# Create your models here.
class Day(models.Model):
    date = models.DateField(auto_now_add=True)

    def __str__(self) -> str:
        return self.date.isoformat()

class Listing(models.Model):
    title = models.CharField(max_length=200)
    website = models.URLField(null=True)
    categories = models.CharField(max_length=400, null=True)
    phone = models.CharField(max_length=30, null=True)
    tag = models.CharField(max_length=400)
    rating = models.DecimalField(max_digits=4, decimal_places=2, null=True)
    reviews = models.IntegerField(null=True)
    latitude = models.CharField(max_length=40)
    longitude = models.CharField(max_length=40)
    address = models.TextField(null=True)
    review_link = models.URLField(null=True)
    cid = models.CharField(max_length=30, unique=True)
    date = models.ForeignKey(Day, null=True, on_delete=models.SET_NULL)

    def __str__(self) -> str:
        return self.title
