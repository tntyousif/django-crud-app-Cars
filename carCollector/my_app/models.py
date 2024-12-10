from django.db import models
from django.urls import reverse
from datetime import date
from django.contrib.auth.models import User

GAS = (
    ('S', 'Super'),
    ('M', 'Mumtaz'),
    ('J', 'Jayyid'),
    ('D', 'Diesel')
)

#Add modification model
class Modification(models.Model):
    name = models.CharField(max_length=50)
    brand = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('modification-detail', kwargs={'pk': self.id})

class Car(models.Model):
    make = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    year = models.IntegerField()
    # Add the M:M relationship
    modifications = models.ManyToManyField(Modification)
    # Add the foreign key linking to the user
    user = models.ForeignKey(User, on_delete=models.CASCADE)


    def __str__(self):
        return self.make + ' ' + self.model
    
    # Define a method to get the URL for this particular car instance
    def get_absolute_url(self):
        # Use the 'reverse' function to dynamically find the URL for viewing this car's details
        return reverse('car-detail', kwargs={'car_id': self.id})
    
class Filling (models.Model):
    date = models.DateField('filling date')
    gas = models.CharField(
        max_length=1,
        choices=GAS,
        default=GAS[0][0]
    )
    car = models.ForeignKey(Car, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_gas_display()} on {self.date}"

