from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MaxValueValidator

# Create your models here.

User = get_user_model()

PROPERTY_TYPE_CHOICES = (())

class Property(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=256)
    description = models.TextField()
    location = models.CharField(max_length=256)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    photo = models.ImageField(upload_to='property_images')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title} at {self.location}"
    

class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    body = models.TextField()
    rating = models.IntegerField(validators=[MaxValueValidator(5)], default=0)
    created_at = models.DateTimeField(auto_now_add=True)

