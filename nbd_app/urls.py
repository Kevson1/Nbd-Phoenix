from django.conf.urls import include, url
from django.urls import path
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^accounts/profile/$', views.profile, name='profile'),
    path('businesses/<neighbourhood_name>/', views.businesses, name='businesses'),
    url(r'^new/generalposts/$', views.create_general_posts, name='create_general_posts'),
    url(r'^new/neighbourhood/$', views.create_neighbourhood, name='create_neighbourhood'),
    url(r'^new/profile/$', views.create_profile, name='create_profile'),
    
]
