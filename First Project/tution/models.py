from django.db import models
from django.utils.timezone import now
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    CATEGORY =(
        ('Teacher' , 'Teacher'),
        ('Student' , 'Student'),
    )
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()
    details = models.TextField(max_length=600)
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    created_at = models.DateTimeField(default=now)

    def __str__(self):
        return self.title 
    
