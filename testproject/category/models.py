from django.db import models

# Create your models here.

class Category(models.Model):
    categoryType=models.CharField(max_length=25)
    def __str__(self):
        return self.categoryType