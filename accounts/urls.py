from django.urls import path
from . views import *
from . import views

urlpatterns = [
    path('', home, name='home'),
    path('aboutus/', aboutus, name='about-us'),
    path('contactus/', contactus, name='contact-us'),
    path('signup/', signup, name='signup'),
    path('login/', login, name='login'),
    path('profile/', profile, name='profile'),  # Add this line
    path('edit-profile/', edit_profile, name='edit-profile'),
    path('cart/', cart, name='cart'),  # Add this line
    path('logout/', logout_view, name='logout'),
    path('password_reset/', CustomPasswordResetView.as_view(), name='password_reset'),
]