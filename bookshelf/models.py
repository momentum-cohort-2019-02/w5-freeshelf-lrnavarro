from django.db import models
from django.utils.text import slugify
from slugger import AutoSlugField

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey('Author', on_delete=models.SET_NULL, null=True)
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the book')
    created_at = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=200)
    # slug = models.SlugField(unique=True)
    slug = AutoSlugField(unique=True, populate_from='title')
    
    def __str__(self):
        return self.title

   
        
#todo:  order booklist by most recent date added


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
