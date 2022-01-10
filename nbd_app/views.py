from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from nbd_app.forms import BusinessForm, GeneralPostsForm, NeighbourhoodForm, PoliceDepForm, ProfileForm, SocialAmenitiesForm


from nbd_app.models import Business, Neighbourhood, Profile,SocialAmenities,GeneralPosts,Police_Department

# Create your views here.
def home(request):
  neighbourhoods = Neighbourhood.get_all_neighbourhoods()
  return render(request, 'home.html', {"neighbourhoods":neighbourhoods})

@login_required(login_url='/accounts/login/')
def profile(request):
  current_user=request.user.id
  profile = Profile.objects.filter(user__id=current_user)
  
  return render(request, 'profile.html', {"profile":profile})

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
    form.instance.user = request.user
    
    form.save()
    return redirect('profile')
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

@login_required(login_url='/accounts/login/')
def create_health_department(request):
  form = SocialAmenitiesForm(request.POST, request.FILES)
  if form.is_valid():
    department_name = form.cleaned_data.get('department_name')
    hotline_number = form.cleaned_data.get('hotline_number')
    email_address = form.cleaned_data.get('email_address')
    neighbourhood = form.cleaned_data.get('neighbourhood')
    
    form.save()
    return redirect('home')
  else:
    form = SocialAmenitiesForm()
    
  return render(request,'new_healthdepartment.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_security_department(request):
  form = PoliceDepForm(request.POST, request.FILES)
  if form.is_valid():
    department_name = form.cleaned_data.get('department_name')
    hotline_number = form.cleaned_data.get('hotline_number')
    email_address = form.cleaned_data.get('email_address')
    neighbourhood = form.cleaned_data.get('neighbourhood')
    
    form.save()
    return redirect('home')
  else:
    form = PoliceDepForm()
  return render(request,'new_securitydepartment.html', {"form":form})

@login_required(login_url='/accounts/login/')
def create_business(request):
  form = BusinessForm(request.POST, request.FILES)
  if form.is_valid():
    business_name = form.cleaned_data.get('business_name')
    business_description = form.cleaned_data.get('business_description')
    business_contact_No = form.cleaned_data.get('business_contact_No')
    business_contact_email = form.cleaned_data.get('business_contact_email')
    neighbourhood = form.cleaned_data.get('neighbourhood')
    
    form.save()
    return redirect('home')
  else:
    form = BusinessForm()
  return render(request,'new_business.html', {"form":form})
