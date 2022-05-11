from django.db import models

# Create your models here.
class Users(models.Model):
    userLogin = models.CharField(
        max_length=255,
    )
    userFirstName = models.CharField(
        max_length=255,
    )
    userLastName = models.CharField(
        max_length=255,
    )
    userPassword = models.CharField(
        max_length=255,
    )

    def __str__(self):
        return ' '.join([
            self.userLogin,
            self.userFirstName,
            self.userLastName,
            self.userPassword
        ])