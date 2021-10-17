from django.test import TestCase
from .models import Profile

#Profile Test class
class ProfileTestClass(TestCase): 
  
  def setUp(self):
    '''Function that runs before every test'''
    self.new_profile = Profile(bio = "I love travelling and watching movies.")
  
  def test_instance(self): 
    '''Test function to confirm that the object actually exists after creation'''
    self.assertTrue(isinstance(self.new_profile,Profile))
    
  def test_save_profile(self): 
    '''Test function testing the save method'''
    self.new_profile.save_profile()
    profiles = Profile.objects.all()
    self.assertTrue(len(profiles) >= 1)
    
  def test_update_profile(self): 
    '''Test function testing update method'''
    self.new_profile.save_profile()
    Profile.objects.filter(bio = "I love travelling and watching movies.").update(bio = "I love hiking")
    updated_profile = Profile.objects.get(bio = "I love hiking")
    self.assertTrue(self.new_profile,updated_profile)
    
  def test_delete_profile(self): 
    '''Test function testing profile delete method'''
    self.new_profile.save_profile()
    self.new_profile.delete_profile()
    after_deletion = Profile.objects.all()
    self.assertTrue(len(after_deletion) == 0)