from django.urls import path
from .views import *

urlpatterns = [
    path('list/', category_list, name='category-list'),
    path('create/', category_create, name='category-create'),
    path('<int:pk>/update/', category_update, name='category-update'),
    path('<int:pk>/delete/', category_delete, name='category-delete'),
    path('<int:category_id>/details/', category_detail, name='category-details'),
    path('<int:category_id>/subcategories/create/', subcategory_create, name='subcategory-create'),
    path('<int:category_id>/subcategories/', subcategory_list, name='subcategory-list'),
    path('<int:category_id>/subcategories/<int:pk>/details/', subcategory_detail, name='subcategory-details'),
    path('subcategories/<int:pk>/update/', subcategory_update, name='subcategory-update'),
    path('subcategories/<int:pk>/delete/', subcategory_delete, name='subcategory-delete'),
]
