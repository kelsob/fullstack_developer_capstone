from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class CarMake(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    # Other fields as needed

    def __str__(self):
        return self.name


class CarModel(models.Model):
    SEDAN = "SEDAN"
    SUV = "SUV"
    COUPE = "COUPE"
    HATCHBACK = "HATCHBACK"
    STATIONWAGON = "STATIONWAGON"
    TRUCK = "TRUCK"

    TYPES = (
        ("SEDAN", "Sedan"),
        ("SUV", "SUV"),
        ("COUPE", "Coupe"),
        ("HATCHBACK", "Hatchback"),
        ("STATIONWAGON", "Station Wagon"),
        ("TRUCK", "Truck"),
        ("VAN", "Van"),
        ("CONVERTIBLE", "Convertible"),
        ("CROSSOVER", "Crossover")
        )
    cartype = models.CharField(max_length=12,
                            choices=TYPES,
                            default="SEDAN")

    name = models.CharField(max_length=100)
    description = models.TextField()
    carmake = models.ForeignKey("CarMake", on_delete=models.CASCADE)
    dealerid = models.IntegerField()
    year = models.IntegerField(default=2000, validators=[MinValueValidator(1), MaxValueValidator(2025)])

    def __str__(self):
        return self.name
