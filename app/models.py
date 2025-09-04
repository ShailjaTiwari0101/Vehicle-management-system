from django.db import models

class Vehicle(models.Model):
    VEHICLE_TYPE_CHOICES = (
        ('Two Wheeler', 'Two Wheeler'),
        ('Three Wheeler', 'Three Wheeler'),
        ('Four Wheeler', 'Four Wheeler'),
    )

    vehicle_number = models.CharField(max_length=20, unique=True)  # Alpha numeric
    vehicle_type = models.CharField(max_length=20, choices=VEHICLE_TYPE_CHOICES)
    vehicle_model = models.CharField(max_length=100)
    vehicle_description = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.vehicle_number} - {self.vehicle_model}"
