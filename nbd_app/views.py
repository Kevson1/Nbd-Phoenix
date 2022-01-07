from django.shortcuts import render

from nbd_app.models import Business

# Create your views here.
def businesses(request):
  businesses = Business.get_all_businesses()
  return render(request, 'businesses.html', {"businesses":businesses})

def general_posts(request):
  pass