from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
from authentication.models import Profile

#Image model
class Image(models.Model): 
  image = CloudinaryField('image')
  image_name = models.CharField(max_length=30)
  image_caption = models.CharField(max_length=100)
  date_added = models.DateTimeField(auto_now_add=True,blank=True,null=True)
  likes = models.IntegerField(default=0)
  comments = models.IntegerField(default=0)
  profile = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  
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

class Follow(models.Model): 
  follower = models.CharField(max_length=1000,null=True)
  user = models.CharField(max_length=1000,null=True)
  
  def __str__(self):
    return str(self.user)
  
class Comment(models.Model):
  image = models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)
  comment = models.CharField(max_length=200)
  posted = models.DateTimeField(auto_now_add=True)

  def save_comment(self):
    self.save()
    
  def delete_comment(self):
    self.delete()

  def __str__(self):
    return self.comment        

class Like(models.Model):
  post = models.ForeignKey(Image,on_delete=models.CASCADE,null=True)
  user = models.ForeignKey(User,on_delete=models.CASCADE,null=True)

  def __str__(self):
    return 'Like by: ' + self.user.username