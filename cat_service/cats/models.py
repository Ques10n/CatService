from django.db import models
from django.contrib.auth.models import User

class Cat(models.Model):
    BREED_CHOICES = [
        ('Siamese', 'Siamese'),
        ('Persian', 'Persian'),
        ('Maine Coon', 'Maine Coon'),
        ('Bengal', 'Bengal'),
    ]

    owner = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    breed = models.CharField(max_length=100, choices=BREED_CHOICES)
    hair_type = models.CharField(max_length=50)

    def __str__(self):
        return self.name
