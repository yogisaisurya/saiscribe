from django.contrib import admin

# Register your models here.
from .models import UserOTP, Scribe, Student

admin.site.register(UserOTP)
admin.site.register(Scribe)
admin.site.register(Student)