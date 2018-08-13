from django.db import models


# Create your models here.
class UserModel(models.Model):
    first_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)
    email = models.EmailField(max_length=50, unique=True)

    def __str__(self):
        return self.first_name
