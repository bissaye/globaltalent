from django.db import models
from django.utils.timezone import now

# Create your models here.
class Rental(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Reservation(models.Model):
    rental_id = models.ForeignKey(Rental, on_delete=models.CASCADE)
    checkin = models.DateField(default=now)
    checkout = models.DateField(null=True)

    def __str__(self):
        return f"Res-{self.id}({self.checkin}, {self.checkout})"