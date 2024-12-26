from django.db import models


# Create your models here.


class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    telegram_id = models.IntegerField(unique=True)
    user_name = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.first_name}  {self.last_name}"


class AuthSms(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=6)

    def __str__(self):
        return f"{self.user.id}- {self.code}"
