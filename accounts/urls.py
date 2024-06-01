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

    path('categorylist/', category_list, name='category-list'),
    path('category/create/', category_create, name='category-create'),
    path('category/<int:pk>/update/', category_update, name='category-update'),
    path('category/<int:pk>/delete/', category_delete, name='category-delete'),
    path('category/<int:category_id>/details/', category_detail, name='category-details'),
    path('category/<int:category_id>/subcategories/create/', subcategory_create, name='subcategory-create'),
    path('category/<int:category_id>/subcategories/', subcategory_list, name='subcategory-list'),
    path('category/<int:category_id>/subcategories/<int:pk>/details/', subcategory_detail, name='subcategory-details'),
    path('category/subcategories/<int:pk>/update/', subcategory_update, name='subcategory-update'),
    path('category/subcategories/<int:pk>/delete/', subcategory_delete, name='subcategory-delete'),

     path('product/list/', product_list, name='product-list'),
    path('product/create/', product_create, name='product-create'),
    path('product/<int:pk>/details', product_details, name='product-details'),
    path('product/<int:pk>/update/', product_update, name='product-update'),
    path('product/<int:pk>/delete/', product_delete, name='product-delete'),
]

