from django.contrib import admin

from nbd_app.models import Business, GeneralPosts, Neighbourhood, Police_Department, Profile, SocialAmenities

# Register your models here.
admin.site.register(Neighbourhood)
admin.site.register(Profile)
admin.site.register(Business)
admin.site.register(SocialAmenities)
admin.site.register(GeneralPosts)
admin.site.register(Police_Department)
