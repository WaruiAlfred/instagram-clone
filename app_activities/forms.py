from django.contrib.auth import models
from django import forms
from django.forms import fields
from .models import Image

class ImagePostForm(forms.ModelForm): 
  class Meta: 
    model = Image
    # exclude = ['date_added','profile']
    fields = ['image','image_name','image_caption']