from django import forms
from .models import Client
from django.core.exceptions import ValidationError
import re

class ClientForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
    
    def clean_client_code(self):
        code = self.cleaned_data['client_code']
        if len(code) < 4:
            raise ValidationError("Client code must be at least 4 characters long.")
        return code

    def clean_contact(self):
        contact = self.cleaned_data['contact']
        if not re.match(r'^[6-9]\d{9}$', contact):
            raise ValidationError("Enter a valid 10-digit Indian mobile number.")
        return contact

    def clean_url(self):
        url = self.cleaned_data['url']
        if url and not url.startswith(('http://', 'https://')):
            raise ValidationError("URL must start with http:// or https://")
        return url

    def clean_project_images(self):
        image = self.cleaned_data.get('project_images')
        if image:
            ext = image.name.split('.')[-1].lower()
            if ext not in ['jpg', 'jpeg', 'png', 'webp']:
                raise ValidationError("Only JPG, JPEG, PNG, and WEBP images are allowed.")
        return image