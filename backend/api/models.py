from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class CustomUser(AbstractUser):
    user_type = models.CharField(max_length=20,choices=[('normal','Normal'),('corporate','Corporate')])

class Role(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name    

class Groups(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

class UserRole(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)

class UserGroup(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    group = models.ForeignKey(Groups, on_delete=models.CASCADE)
