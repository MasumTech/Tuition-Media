from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
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
    image = models.ImageField(default='default.png', upload_to='tution/images/')
    created_at = models.DateTimeField(default=now)
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super(Post, self).save(*args, **kwargs)
        img = Image.open(self.image.path)
        if img.height > 300 or img.width >300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
        
    def __str__(self):
        return self.title 
    
