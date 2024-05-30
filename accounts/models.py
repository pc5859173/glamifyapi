from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from product. models import Product

class CustomUser(AbstractUser):
    agreed_to_terms = models.BooleanField(default=False)
    groups = models.ManyToManyField(Group,related_name='customuser_set',blank=True,
    help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.',related_query_name='user',)
    user_permissions = models.ManyToManyField(Permission, related_name='customuser_set', blank=True, help_text='Specific permissions for this user.',related_query_name='user',)

class Profile(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='profile')
    bio = models.TextField(blank=True, null=True)
    avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    # Add other profile fields as necessary

    def __str__(self):
        return self.user.username
    
class Cart(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='cart')
    products = models.ManyToManyField(Product, through='CartItem')

    def __str__(self):
        return f"{self.user.username}'s cart"

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.quantity} of {self.product.name} in {self.cart.user.username}'s cart"    