from django.urls import path
from . views import *

urlpatterns = [
    path('list/', product_list, name='product-list'),
    path('create/', product_create, name='product-create'),
    path('<int:pk>/details', product_details, name='product-details'),
    path('<int:pk>/update/', product_update, name='product-update'),
    path('<int:pk>/delete/', product_delete, name='product-delete'),
]