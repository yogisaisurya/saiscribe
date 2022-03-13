from django.db import models
from django.contrib.auth.models import User

class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField(default=0)

	def __str__(self):
		return str(self.user)

class Scribe(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	sc_st = models.CharField(max_length=13, default = "Scribe")
	age = models.IntegerField(default=0)
	phone = models.BigIntegerField(default=0)
	qualification = models.CharField(max_length=40, default = "")
	qual_course = models.CharField(max_length=40, default = "")
	location = models.CharField(max_length=40, default = "")
	pincode = models.BigIntegerField(default=0)
	lang1 = models.CharField(max_length=40, default = "")
	lang2 = models.CharField(max_length=40, default = "")
	lang3 = models.CharField(max_length=40, default = "")
	classes = models.CharField(max_length=40, default = "")
	course = models.CharField(max_length=40, default = "")
	paid_unpaid = models.CharField(max_length=40, default = "")

	def __str__(self):
		return str(self.user)

class Student(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	sc_st = models.CharField(max_length=13, default = "Student")
	age = models.IntegerField(default=0)
	phone = models.BigIntegerField(default=0)
	disability = models.CharField(max_length=40, default = "")
	classes = models.CharField(max_length=40, default="")
	course = models.CharField(max_length=40, default="")
	lang = models.CharField(max_length=40, default="")
	pref_lang = models.CharField(max_length=40, default="")
	school = models.CharField(max_length=40, default = "")
	paid_unpaid = models.CharField(max_length=40, default="")
	location = models.CharField(max_length=40, default = "")
	pincode = models.BigIntegerField(default=0)

	def __str__(self):
		return str(self.user)


# Create your models here.
