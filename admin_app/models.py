from django.db import models

# Create your models here.

class add_product(models.Model):

    CATEGORY_CHOICES = [
       ('Fresh_Products', 'Fresh Products'),
       ('Dairy_Eggs', 'Dairy Eggs'),
       ('Meat_Seafood', 'Meat Seafood'),
       ('Pantry', 'Pantry'),
       ('Frozen_Products', 'Frozen Products'),
       ('Snacks_Bakery', 'Snacks Bakery'),
       ('Drinks', 'Drinks'),
       ('Homeware', 'Homeware'),
    ]
    
    product_image = models.ImageField()
    product_invoice = models.CharField(max_length=50)
    product_name = models.CharField(max_length=250)
    product_description = models.CharField(max_length=500)
    product_brand = models.CharField(max_length=100)
    product_price = models.IntegerField()
    product_offer_price = models.IntegerField(null=True, blank=True)
    product_size = models.CharField(max_length=50)
    product_offer = models.IntegerField(null=True, blank=True)
    product_category = models.CharField(max_length=50, choices=CATEGORY_CHOICES)