from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from nbd_app.models import Business, Neighbourhood,SocialAmenities,GeneralPosts,Police_Department

# Create your views here.
def home(request):
  neighbourhoods = Neighbourhood.get_all_neighbourhoods()
  return render(request, 'home.html', {"neighbourhoods":neighbourhoods})

@login_required(login_url='/accounts/login/')
def profile(request):
  return render(request, 'profile.html')

@login_required(login_url='/accounts/login/')
def businesses(request, neighbourhood_name):
  businesses = Business.filter_by_neighbourhood(neighbourhood_name)
  health_info = SocialAmenities.filter_by_neighbourhood(neighbourhood_name)
  security_info = Police_Department.filter_by_neighbourhood(neighbourhood_name)
  general_posts = GeneralPosts.filter_by_neighbourhood(neighbourhood_name)
  return render(request, 'businesses.html', {"businesses":businesses, "health_info":health_info, "security_info":security_info, "general_posts":general_posts})

@login_required(login_url='/accounts/login/')
def general_posts(request):
  return render(request,'generalposts.html')

@login_required(login_url='/accounts/login/')
def social_amenities(request):
  return render(request, 'socialamenities.html')