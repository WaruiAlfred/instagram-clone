from django.test import TestCase
from .models import Image
from authentication.models import Profile
from django.contrib.auth.models import User
   
#Image test class
class ImageTestClass(TestCase): 
  
  def setUp(self): 
    '''Function that runs before every test'''
    
    #creating a new user
    self.new_user = User.objects.create(id=10,username='tester',email="tester@gmail.com",password="testing321")
    #creating a new profile and saving it
    self.user_profile = Profile(bio = "Photo-phobia ain't my thing.",user=self.new_user)
    self.user_profile.save_profile()
    
    #creating a new image model
    self.new_image = Image(image_name = "Code",
                           image_caption = "Coding is my cardio",
                           likes=500,
                           comments=2,
                           profile=self.user_profile,
                           user=self.new_user)
  def tearDown(self):
    User.objects.all().delete()
    Profile.objects.all().delete()
    Image.objects.all().delete()
    
  def test_save_method(self): 
    '''Function testing the save method'''
    self.new_image.save_image()
    images = Image.objects.all()
    self.assertTrue(len(images)>0)