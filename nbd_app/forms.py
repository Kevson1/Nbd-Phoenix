from django import forms
from .models import Profile, GeneralPosts

class ProfileForm(forms.ModelForm):
  class Meta:
    model = Profile
    fields = ['first_name', 'last_name','id_number', 'profile_pic', 'neighbourhood']
   
class GeneralPostsForm(forms.ModelForm):
  class Meta:
    model = GeneralPosts
    fields = ['topic', 'title', 'message', 'neighbourhood']
