from django.db import models
from admin_app.models import add_product
from veva.models import user_register


# Create your models here.

class additional_info(models.Model):
    user_address = models.CharField(max_length=255, null=True, blank=True)
    user_state = models.CharField(max_length=100, null=True, blank=True)
    user_pincode = models.CharField(max_length=20, null=True, blank=True)
    user_dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)

class Wishlist(models.Model):
    user_id = models.IntegerField() 
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('user_id', 'product')

    def __str__(self):
        return f'User {self.user_id} - {self.product.product_name}'
    
class Shipping_address(models.Model):

    STATE_CHOICES = [
        ("KL", "Kerala"),
        ("KA", "Karnataka"),
        ("TN", "Tamil Nadu"),
    ]

    user = models.ForeignKey('veva.user_register', on_delete=models.CASCADE, null=True, blank=True)
    full_name   = models.CharField(max_length=120)
    mobile      = models.CharField(max_length=15)
    pincode     = models.CharField(max_length=10)
    locality    = models.CharField(max_length=150)
    address_line = models.TextField()
    city        = models.CharField(max_length=100)
    state       = models.CharField(max_length=2, choices=STATE_CHOICES)
    landmark    = models.CharField(max_length=150, blank=True)
    alt_phone   = models.CharField(max_length=15, blank=True)
    

class Cart(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    product = models.ForeignKey(add_product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    added_at = models.DateTimeField(auto_now_add=True)


class Order_details(models.Model):
    user = models.ForeignKey(user_register, on_delete=models.CASCADE)
    product = models.TextField()  # You can store JSON string of product name, qty, price
    address = models.ForeignKey(Shipping_address, on_delete=models.CASCADE)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.CharField(max_length=20)  # COD or UPI
    payment_status = models.CharField(max_length=20)  # Paid or Unpaid
    status = models.CharField(max_length=20, default='Pending')  # Pending / Completed
    created_at = models.DateTimeField(auto_now_add=True)