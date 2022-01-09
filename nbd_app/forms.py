from django import forms
from .models import Neighbourhood, Profile, GeneralPosts

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
    