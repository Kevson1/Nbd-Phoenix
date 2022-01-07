from django.shortcuts import render

# Create your views here.
def businesses(request):
  
  return render(request, 'index.html')