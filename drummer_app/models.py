from django.db import models
from django.contrib.auth import get_user_model


class Band(models.Model):
    name = models.CharField(max_length=100)


# Create your models here.
class Drummer(models.Model):
    name = models.CharField(max_length=100)
    band = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    drum_brand = models.CharField(max_length=100)
    genre = models.CharField(max_length=100)
    active = models.BooleanField(default=False)   
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
