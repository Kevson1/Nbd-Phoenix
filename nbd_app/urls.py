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
    url(r'^new/health_department/$', views.create_health_department, name='create_health_department'),
    url(r'^new/security_department/$', views.create_security_department, name='create_security_department'),
    url(r'^new/business/$', views.create_business, name='create_business'),
]
