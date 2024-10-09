from django.db import models

# Create your models here.
class UserRegistration(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField()
    mobile = models.BigIntegerField(default=0)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.first_name