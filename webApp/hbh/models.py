from django.db import models

class User(models.Model):
    UserName = models.CharField(max_length=30)
    UserPassword = models.CharField(max_length=30)
    PhoneNumber = models.CharField(max_length=30)
    Data = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.UserName