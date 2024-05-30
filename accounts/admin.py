from django.contrib import admin
from .models import CustomUser, Profile, Product, Cart, CartItem
from django.contrib.auth.admin import UserAdmin

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline,)

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Cart)
admin.site.register(CartItem)
