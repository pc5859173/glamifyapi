from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import CustomUser

from django import forms
from django.contrib.auth.models import User

from django import forms
from .models import Category, Subcategory
from django import forms
from .models import Product

class SignupForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

class LoginForm(AuthenticationForm):
    class Meta:
        model = CustomUser
        fields = ['username', 'password']


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']  # Customize fields as needed



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name', 'description', 'image']  # Specify the fields you want in the form

class SubcategoryForm(forms.ModelForm):
    class Meta:
        model = Subcategory
        fields = ['category', 'name',  'image']   
        widgets = {
            'category': forms.Select(attrs={'class': 'form-control'})
        }     

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['subcategory', 'name', 'description', 'price', 'quantity', 'image', ]