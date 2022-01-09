from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from nbd_app.forms import GeneralPostsForm, NeighbourhoodForm, ProfileForm


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
def create_general_posts(request):
  form = GeneralPostsForm(request.POST, request.FILES)
  if form.is_valid():
    topic = form.cleaned_data.get('topic')
    title = form.cleaned_data.get('title')
    message = form.cleaned_data.get('message')
    neighbourhood = form.cleaned_data.get('neighbourhood')
    
    form.save()
    return redirect('home')
  else:
    form = GeneralPostsForm()
    
  return render(request,'generalposts.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_profile(request):
  form = ProfileForm(request.POST, request.FILES)
  if form.is_valid():
    first_name = form.cleaned_data.get('first_name')
    last_name = form.cleaned_data.get('last_name')
    id_number = form.cleaned_data.get('id_number')
    profile_pic = form.cleaned_data.get('profile_pic')
    neighbourhood = form.cleaned_data.get('neighbourhood')
    
    form.save()
    return redirect('home')
  else:
    form = ProfileForm()
    
  return render(request,'new_profile.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_neighbourhood(request):
  form = NeighbourhoodForm(request.POST, request.FILES)
  if form.is_valid():
    neighbourhood_name = form.cleaned_data.get('neighbourhood_name')
    general_location = form.cleaned_data.get('general_location')
    
    form.save()
    return redirect('home')
  else:
    form = NeighbourhoodForm()
  return render(request, 'new_neighbourhood.html', {"form":form})

@login_required(login_url='/accounts/login/')
def social_amenities(request):
  return render(request, 'socialamenities.html')

  topic = models.CharField(max_length=20)
  title = models.CharField(max_length=100)
  message = models.TextField()
  date_posted = models.DateTimeField(auto_now=True)
  neighbourhood 