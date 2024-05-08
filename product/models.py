from django.db import models
from category.models import Category, Subcategory

class Product(models.Model):
    subcategory = models.ForeignKey(Subcategory, related_name='products', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)
    image = models.ImageField(upload_to='products/' ,blank=True, null=True)

    def __str__(self):
        return self.name

