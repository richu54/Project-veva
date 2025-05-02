from django.db import models

# Create your models here.

class user_register(models.Model):
    user_email = models.CharField(max_length=255)
    user_password = models.CharField(max_length=100)
    user_name = models.CharField(max_length=100)
    user_mobile = models.CharField(max_length=60)
    registered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_email