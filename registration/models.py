from django.db import models

# Create your models here.
class Vehicle(models.Model):
    voucher_no = models.CharField(max_length=20, unique=True)
    registration_plate = models.CharField(max_length=15, unique=True)
    contact_no = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.registration_plate} ({self.voucher_no})"
