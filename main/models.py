from django.db import models

class Sneaker(models.Model):
    BRAND_CHOICES = (
        ('Nike', 'Nike'),
        ('Adidas', 'Adidas'),
        ('Puma', 'Puma'),
    )

    COLOR_CHOICES = (
        ('Red', 'Red'),
        ('Blue', 'Blue'),
        ('Black', 'Black'),
    )

    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50, choices=BRAND_CHOICES)
    color = models.CharField(max_length=50, choices=COLOR_CHOICES)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    description = models.TextField()
    image_url = models.URLField()
    website_url = models.URLField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
