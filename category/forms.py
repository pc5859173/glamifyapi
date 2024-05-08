from django import forms
from .models import Category, Subcategory

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
