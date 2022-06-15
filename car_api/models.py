from django.db import models
from django.contrib.auth.models import User

class Car(models.Model):
    vehicle_name = models.CharField(max_length=20)
    vehicle_number = models.CharField(max_length=20)
    model = models.CharField(max_length=50)
    availability = models.BooleanField(null=True)
    
    class Rent(models.TextChoices):
        AC_1500 = '1500'
        Non_AC_1000 = '1000'
        
    rent_type = models.CharField(
        max_length=50, choices=Rent.choices, default=Rent.AC_1500)

    def __str__(self):
        return self.vehicle_name


class Reservation(models.Model):
    class Payment(models.TextChoices):
        card_payment = 'card payment'
        Direct_payment = 'Direct payment'

    customer = models.ForeignKey('account.User', on_delete=models.CASCADE)
    car = models.ForeignKey(Car, on_delete=models.CASCADE)
    
    payment_type = models.CharField(
        max_length=50, choices=Payment.choices, default=Payment.card_payment)
    issue_date = models.DateField()
    return_date = models.DateField()

    def __str__(self):
        return str(self.customer) + "- " + str(self.car)
