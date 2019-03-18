from django.conf import settings
from django.db import models
from django.urls import reverse
# from django.utils.text import slugify
from slugger import AutoSlugField




class Author(models.Model):
    name = models.CharField(max_length=200,)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, related_name ="books", max_length=200, blank=True, null=True,  on_delete=models.SET_NULL)
    category = models.CharField(max_length=200, blank=True, null=True)
    description = models.TextField(max_length=1000)
    created_at = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=200)
    # slug = models.SlugField(unique=True)
    slug = AutoSlugField(unique=True, max_length=200, populate_from='title')
    # book_cover = models.ImageField(upload_to='books', blank=True, null=True)
    
    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"pk": self.pk})    

   #order booklist by most recent date added to database
    class Meta:
        ordering = ['-created_at']



    
