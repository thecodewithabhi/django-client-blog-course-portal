from django.db import models

# Create your models here.

PROJECT_STATUS_CHOICES = [
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
    ('on_hold', 'On Hold'),
    ('cancelled', 'Cancelled'),
]

class Client(models.Model):
    client_code = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    contact = models.CharField(max_length=15)
    address = models.TextField()
    description = models.TextField(blank=True, null=True)
    url_link = models.URLField(blank=True, null=True)
    project_status = models.CharField(
        max_length=20,
        choices=PROJECT_STATUS_CHOICES,
        default='ongoing'
    )

    def __str__(self):
        return f"{self.name} ({self.client_code})"

# Model to store multiple images per client
class ProjectImage(models.Model):
    client = models.ForeignKey(Client, related_name='project_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='client_projects/')
    caption = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f"Image for {self.client.name}"