from django.test import TestCase
from .models import Neighbourhood, Profile, GeneralPosts, SocialAmenities, Business

# Create your tests here.
class NeighbourhoodTestCase(TestCase):
  #Set up method
  def setUp(self):
    self.nbd = Neighbourhood(neighbourhood_name='Makongeni', general_location='Kaloleni')
    
  #Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.nbd, Neighbourhood))
  
  #Test save neighbourhood
  def test_save_nbd(self):
    self.nbd.save_nbd()
    neighbourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighbourhoods)==1)
    

class ProfileTestCase(TestCase):
  pass

class SocialAmenitiesTestCase(TestCase):
  pass

class BusinessTestCase(TestCase):
  pass

class GeneralPostsTestCase(TestCase):
  pass
