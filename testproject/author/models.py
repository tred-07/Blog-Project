from django.db import models
from django.contrib.auth.models import User
from category.models import Category
# Create your models here.


class Blog(models.Model):
    title=models.CharField(max_length=40)
    description=models.TextField()
    author=models.ForeignKey(User,on_delete=models.CASCADE)
    date=models.DateTimeField()
    category=models.ManyToManyField(Category)

    def __str__(self):
        return f'{self.title}'