from django.db import models
from admin_app.models import add_product


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