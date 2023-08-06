from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=250)
    subtitle = models.CharField(max_length=250, blank=True, null=True)
    authors = models.CharField(max_length=100, verbose_name="Author(s)", blank=True, null=True)
    isbn = models.CharField(max_length=13, blank=True, null=True)
    asin = models.CharField(max_length=10, blank=True, null=True)

    def __str__(self):
        return self.title
    
