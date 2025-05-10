from django.db import models

# Create your models here.

class additional_info(models.Model):
    user_address = models.CharField(max_length=255, null=True, blank=True)
    user_state = models.CharField(max_length=100, null=True, blank=True)
    user_pincode = models.CharField(max_length=20, null=True, blank=True)
    user_dob = models.DateField(null=True, blank=True)
    gender = models.CharField(max_length=10, null=True, blank=True)
