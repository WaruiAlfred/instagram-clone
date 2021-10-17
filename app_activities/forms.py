from django.contrib.auth import models
from django import forms
from django.forms import fields
from .models import Image,Comment

class ImagePostForm(forms.ModelForm): 
  class Meta: 
    model = Image
    # exclude = ['date_added','profile']
    fields = ['image','image_name','image_caption']
    
class CommentForm(forms.ModelForm):
  class Meta:
    model = Comment
    exclude = ['user','image','posted_on']