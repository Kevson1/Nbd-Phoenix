from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Neighbourhood(models.Model):
  neighbourhood_name = models.CharField(max_length=25)
  general_location = models.CharField(max_length=25)
  
  def save_nbd(self):
    self.save()
    
  def delete_nbd(self):
    self.delete()
    
  @classmethod 
  def get_all_neighbourhoods(cls):
    all_projects = cls.objects.all()
    return all_projects
  
  def __str__(self):
    return self.neighbourhood_name
  
class Profile(models.Model):
  first_name = models.CharField(max_length=20)
  last_name = models.CharField(max_length=20)
  id_number = models.IntegerField()
  profile_pic = models.ImageField(upload_to='static/images/', null=True)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  
  def save_profile(self):
    self.save()
    
  def delete_profile(self):
    self.delete()
  
  def __str__(self):
    return self.first_name
  
class SocialAmenities(models.Model):
  department_name = models.CharField(max_length=30)
  hotline_number = models.BigIntegerField()
  email_address = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  
  def save_amenity(self):
    self.save()
    
  def delete_amenity(self):
    self.delete()
    
  @classmethod
  def filter_by_neighbourhood(cls, neighbourhood_search):
    found_amenities = cls.objects.filter(neighbourhood__neighbourhood_name = neighbourhood_search)
    return found_amenities
  
  
  def __str__(self):
    return self.department_name
  
class Police_Department(models.Model):
  department_name = models.CharField(max_length=30)
  hotline_number = models.BigIntegerField()
  email_address = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  
  def save_department(self):
    self.save()
    
  def delete_department(self):
    self.delete()
    
  @classmethod
  def filter_by_neighbourhood(cls, neighbourhood_search):
    found_department = cls.objects.filter(neighbourhood__neighbourhood_name = neighbourhood_search)
    return found_department
  
  
  def __str__(self):
    return self.department_name
  
class Business(models.Model):
  business_name = models.CharField(max_length=30)
  business_description = models.TextField()
  business_contact_No = models.BigIntegerField()
  business_contact_email = models.EmailField()
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  
  def save_business(self):
    self.save()
    
  def delete_business(self):
    self.delete()
    
  @classmethod 
  def get_all_businesses(cls):
    all_projects = cls.objects.all()
    return all_projects
    
  @classmethod
  def filter_by_neighbourhood(cls, neighbourhood_search):
    found_amenities = cls.objects.filter(neighbourhood__neighbourhood_name = neighbourhood_search)
    return found_amenities
  
  def __str__(self):
    return self.business_name
  
class GeneralPosts(models.Model):
  topic = models.CharField(max_length=20)
  title = models.CharField(max_length=100)
  message = models.TextField()
  date_posted = models.DateTimeField(auto_now=True)
  neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE)
  
  def save_news(self):
    self.save()
    
  def delete_news(self):
    self.delete()
    
  @classmethod
  def filter_by_neighbourhood(cls, neighbourhood_search):
    found_amenities = cls.objects.filter(neighbourhood__neighbourhood_name = neighbourhood_search)
    return found_amenities
  
  def __str__(self):
    return self.title
  
  