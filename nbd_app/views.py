from django.shortcuts import render
from django.contrib.auth.decorators import login_required


from nbd_app.models import Business

# Create your views here.
@login_required(login_url='/accounts/login/')
def businesses(request):
  businesses = Business.get_all_businesses()
  return render(request, 'businesses.html', {"businesses":businesses})

@login_required(login_url='/accounts/login/')
def general_posts(request):
  return render(request,'generalposts.html')

@login_required(login_url='/accounts/login/')
def social_amenities(request):
  return render(request, 'socialamenities.html')