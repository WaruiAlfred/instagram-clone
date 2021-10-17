from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from authentication.models import Profile

#Profile model
# class Profile(models.Model): 
#   profile_photo = CloudinaryField('image')
#   bio = models.TextField(blank=True)

#   def save_profile(self): 
#     '''function to save profile details'''
#     self.save()
    
#   def update_profile(self): 
#     '''Function to update profile'''
#     Profile.objects.filter(id = self.id).update(bio = self.bio)
#     self.save()
    
#   def delete_profile(self): 
#     '''Function to delete a profile object'''
#     profile = Profile.objects.get(id = self.id)
#     if profile: 
#       profile.delete()

#   def __str__(self):
#     return self.bio

#Image model
class Image(models.Model): 
  image = CloudinaryField('image')
  image_name = models.CharField(max_length=30)
  image_caption = models.CharField(max_length=50)
  date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  likes = models.IntegerField()
  comments = models.CharField(max_length=100)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE)
  
  def save_image(self): 
    '''function to save an image and its details'''
    self.save()
    
  def update_caption(self): 
    '''Function to update caption'''
    Image.objects.filter(id = self.id).update(image_caption = self.image_caption)
    self.save()
    
  def delete_image(self): 
    '''Function to delete an image object'''
    image = Image.objects.get(id = self.id)
    if image: 
      image.delete()
    
  def __str__(self):
    return self.image_name
