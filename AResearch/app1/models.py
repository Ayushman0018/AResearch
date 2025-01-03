from django.db import models

# Create your models here.
class user(models.Model):
    username = models.TextField(default='')
    psw = models.TextField(default='')
    otp = models.TextField(default='')
    email = models.TextField(default='')
    active = models.TextField(default="FALSE")
    def __str__(self):
        return f"{self.username} - {self.email}"