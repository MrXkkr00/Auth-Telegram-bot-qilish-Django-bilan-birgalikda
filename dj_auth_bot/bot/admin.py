from django.contrib import admin

# Register your models here.
from .models import User, AuthSms

admin.site.register(User)
admin.site.register(AuthSms)