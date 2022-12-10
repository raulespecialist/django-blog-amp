import os
from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from django.template.defaultfilters import slugify

def create_slug_page(title): # new
       slug = slugify(title)
       qs = Page.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug

def create_slug_post(title): # new
       slug = slugify(title)
       qs = Post.objects.filter(slug=slug)
       exists = qs.exists()
       if exists:
           slug = "%s-%s" %(slug, qs.first().id)
       return slug

class Page(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, default='')
    category = models.CharField(max_length=50, default='')
    image_cover = models.ImageField(upload_to = 'images/', blank=True)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
      return reverse('page_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
         if not self.slug:
            self.slug = create_slug_page(self.title)
         return super().save(*args, **kwargs)

class PageImage(models.Model):
    page = models.ForeignKey(Page, default=None, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to = 'images/', blank=True)

    def filename_minus_extension(self): 
        basename, extension = os.path.splitext(os.path.basename(self.images.name)) 
        return basename


    def __str__(self):
        return self.page.title

class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, null=True, blank=True, unique=True, default='')
    image_cover = models.ImageField(upload_to = 'images/', blank=True)
    text = models.TextField()
    page = models.ForeignKey(Page, on_delete=models.CASCADE, related_name="posts")
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
      return reverse('post_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs): # new
         if not self.slug:
            self.slug = create_slug_post(self.title)
         return super().save(*args, **kwargs)

class PostImage(models.Model):
    post = models.ForeignKey(Post, default=None, on_delete=models.CASCADE, related_name="images")
    images = models.ImageField(upload_to = 'images/')
 
    def __str__(self):
        return self.post.title