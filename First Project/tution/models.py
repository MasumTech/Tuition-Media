from django.db import models
from django.utils.timezone import now
from PIL import Image
from django.utils.text import slugify
from multiselectfield import MultiSelectField
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField()
    
    def __str__(self):
        return self.name

class Subject(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Class_in(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name
        

    
class Post(models.Model):
    CATEGORY =(
        ('Teacher' , 'Teacher'),
        ('Student' , 'Student'),
    )
    MEDIUM =(
        ('Bangla', 'Bangla'),
        ('English', 'English'),
        ('Arabic', 'Arabic'),
        ('Hindi', 'Hindi'),
        ('Urdu', 'Urdu'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    slug = models.CharField(max_length=100, default=title)
    email = models.EmailField(max_length=100)
    salary = models.IntegerField()
    details = models.TextField(max_length=600)
    available = models.BooleanField()
    category = models.CharField(max_length=100, choices=CATEGORY)
    image = models.ImageField(default='default.png', upload_to='tution/images/')
    medium = MultiSelectField(max_length=100, max_choices=5, choices=MEDIUM, default='Bangla')
    subject = models.ManyToManyField(Subject, related_name='subject_set')
    class_in = models.ManyToManyField(Class_in, related_name='class_set')
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
    
