from django.db import models
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField 

# Create your models here.
def validate_duration(value):
    if value <= 0:
        raise ValidationError("Duration must be a positive number.")

class Course(models.Model):
    name = models.CharField(max_length=200)
    duration = models.PositiveIntegerField(help_text="Duration in hours", validators=[validate_duration])
    description = RichTextField()

    def __str__(self):
        return self.name

class Module(models.Model):
    course = models.ForeignKey(Course, related_name='modules', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    content = RichTextField()
    photo = models.ImageField(upload_to='module_photos/', blank=True, null=True)
    def __str__(self):
        return f"{self.title} ({self.course.name})"