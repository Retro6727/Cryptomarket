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
    
class CryptoConversion(models.Model):
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    from_currency = models.CharField(max_length=10)
    to_currency = models.CharField(max_length=10)
    converted_amount = models.DecimalField(max_digits=20, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.amount} {self.from_currency} to {self.to_currency}"