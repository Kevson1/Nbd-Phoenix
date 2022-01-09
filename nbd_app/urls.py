from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^businesses/$', views.businesses, name='businesses'),
    url(r'^generalposts/$', views.general_posts, name='general_posts'),
    url(r'^socialamenities/$', views.social_amenities, name='social_amenities'),
]
