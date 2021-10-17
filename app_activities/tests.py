from django.test import TestCase
from .models import Image
from authentication.models import Profile
   
#Image test class
class ImageTestClass(TestCase): 
  
  def setUp(self): 
    '''Function that runs before every test'''
    
    #creating a new profile and saving it
    self.user_profile = Profile(bio = "Photo-phobia ain't my thing.")
    self.user_profile.save_profile()
    
    #creating a new image model
    self.new_image = Image(image_name = "Code",
                           image_caption = "Coding is my cardio",
                           likes=500,
                           comments="")