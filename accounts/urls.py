from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='about-us'),
    path('contactus/', contactus, name='contact-us'),
]