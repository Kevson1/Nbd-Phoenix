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
    
  # Test_delete_neighbourhood
  def test_delete_nbd(self):
    self.nbd.save_nbd()
    self.nbd.delete_nbd()
    neighbourhoods = Neighbourhood.objects.all()
    self.assertTrue(len(neighbourhoods)==0)
    

class ProfileTestCase(TestCase):
  # Set up method
  def setUp(self):
    # Create a neighbourhood instance
    self.nbd = Neighbourhood(neighbourhood_name='Makongeni', general_location='Kaloleni')
    self.nbd.save_nbd()
    
    # Create a profile instance
    self.profile = Profile(first_name = 'kelvin', last_name = 'kimani', id_number = '123456', profile_pic = 'my_picture', neighbourhood = self.nbd)
    self.profile.save_profile()
    
  # Teardown method
  def tearDown(self):
    Neighbourhood.objects.all().delete()
    Profile.objects.all().delete()
    
  # Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.profile, Profile))
    
  # Test save profile method
  def test_save_profile(self):
    self.profile.save_profile()
    saved_profiles = Profile.objects.all()
    self.assertTrue(len(saved_profiles)==1)
    
  # Test delete profile method
  def test_delete_profile(self):
    self.profile.save_profile()
    self.profile.delete_profile()
    existing_profiles = Profile.objects.all()
    self.assertTrue(len(existing_profiles)==0)
    

class SocialAmenitiesTestCase(TestCase):
  # Set up method
  def setUp(self):
    # Create a Neighbourhood instance
    self.nbd = Neighbourhood(neighbourhood_name='Makongeni', general_location='Kaloleni')
    self.nbd.save_nbd()
    
    # Create a social Amenities instance
    self.socialAmenity = SocialAmenities(department_name = 'health', hotline_number = '+254789654112', email_address = 'health@kenya.gmail.com', neighbourhood = self.nbd)
    self.socialAmenity.save_amenity()
    
  # Teardown method
  def tearDown(self):
    Neighbourhood.objects.all().delete()
    SocialAmenities.objects.all().delete()
    
  # Test instance
  def test_instance(self):
    self.assertTrue(isinstance(self.socialAmenity, SocialAmenities))

  # Test save amenity
  def test_save_amenity(self):
    self.socialAmenity.save_amenity()
    available_amenities = SocialAmenities.objects.all()
    self.assertTrue(len(available_amenities)==1)
  
  # Test delete amenity  
  def test_delete_amenity(self):
    self.socialAmenity.save_amenity()
    self.socialAmenity.delete_amenity()
    available_amenities = SocialAmenities.objects.all()
    self.assertTrue(len(available_amenities)==0)
    
  # Filter by neighbourhood
  def test_filter_by_neighbourhood(self):
    # Create a Neighbourhood instance
    self.nbd = Neighbourhood(neighbourhood_name='Huruma', general_location='Kaloleni')
    self.nbd.save_nbd()
    
    # Create a social Amenities instance
    self.socialAmenity = SocialAmenities(department_name = 'health', hotline_number = '+254789654112', email_address = 'health@kenya.gmail.com', neighbourhood = self.nbd)
    self.socialAmenity.save_amenity()
    
    amenities_found_for_nbd = SocialAmenities.filter_by_neighbourhood('Huruma')
    self.assertTrue(len(amenities_found_for_nbd)==1)
    
    
# class BusinessTestCase(TestCase):
#   pass

# class GeneralPostsTestCase(TestCase):
#   pass
