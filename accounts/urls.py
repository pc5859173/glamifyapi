from django.urls import path
from . views import *

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='about-us'),
    path('contactus/', contactus, name='contact-us'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]