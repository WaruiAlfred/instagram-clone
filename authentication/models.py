from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
from PIL import Image

class Profile(models.Model): 
  user = models.OneToOneField(User,on_delete=models.CASCADE)
  profile_photo = CloudinaryField('image',default='static/images/default.png')
  bio = models.TextField(blank=True)
  
  def save_profile(self): 
    '''function to save profile details'''
    super().save()
    
    img = Image.open(self.profile_photo.path)
    if img.height > 300 or img.width > 300: 
      output_size = (300,300)
      img.thumbnail(output_size)
      img.save(self.profile_photo.path)
    
  def update_profile(self): 
    '''Function to update profile'''
    Profile.objects.filter(id = self.id).update(bio = self.bio)
    self.save()
    
  def delete_profile(self): 
    '''Function to delete a profile object'''
    profile = Profile.objects.get(id = self.id)
    if profile: 
      profile.delete()
  
  def __str__(self):
    return f'{self.user.username} profile'
