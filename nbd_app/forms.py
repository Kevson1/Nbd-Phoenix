from django import forms
from .models import Business, Neighbourhood, Police_Department, Profile, GeneralPosts, SocialAmenities

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name', 'last_name','id_number', 'profile_pic', 'neighbourhood']
   
class GeneralPostsForm(forms.ModelForm):
  class Meta:
    model = GeneralPosts
    fields = ['topic', 'title', 'message', 'neighbourhood']

class NeighbourhoodForm(forms.ModelForm):
  class Meta:
    model = Neighbourhood
    fields = ['neighbourhood_name', 'general_location']
    
class SocialAmenitiesForm(forms.ModelForm):
  class Meta:
    model = SocialAmenities
    fields = ['department_name', 'hotline_number', 'email_address', 'neighbourhood']
    
class PoliceDepForm(forms.ModelForm):
  class Meta:
    model = Police_Department
    fields = ['department_name', 'hotline_number', 'email_address', 'neighbourhood']
    
class BusinessForm(forms.ModelForm):
  class Meta:
    model = Business
    fields = ['business_name', 'business_description', 'business_contact_No', 'business_contact_email', 'neighbourhood']
    