from django.db import models

from django.core.exceptions import ValidationError
from django.utils.text import slugify
from ckeditor.fields import RichTextField 
from django.utils import timezone
from member.models import Client  


# Blog status choices
BLOG_STATUS_CHOICES = [
    ('draft', 'Draft'),
    ('published', 'Published'),
]

def validate_title_length(value):
    if len(value) < 5:
        raise ValidationError('Title must be at least 5 characters long.')

def validate_image_extension(value):
    valid_extensions = ['jpg', 'jpeg', 'png', 'webp']
    if not value.name.split('.')[-1].lower() in valid_extensions:
        raise ValidationError('Only JPG, PNG, and WEBP images are allowed.')

class Blog(models.Model):
    author = models.ForeignKey(Client, related_name='blogs', on_delete=models.CASCADE)
    title = models.CharField(max_length=200, validators=[validate_title_length])
    slug = models.SlugField(unique=True, blank=True)
    content = RichTextField()
    thumbnail = models.ImageField(upload_to='blog_thumbnails/', validators=[validate_image_extension])
    status = models.CharField(max_length=10, choices=BLOG_STATUS_CHOICES, default='draft')
    published_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)
