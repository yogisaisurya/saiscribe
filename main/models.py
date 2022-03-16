from django.db import models
from django.contrib.auth.models import User

classes_choice = (
    ('Select', 'Select'),
	('Class 10th', 'Class 10th'),
	('Class 12th', 'Class 12th'),
    ('Both Class 10th & Class 12th', 'Both Class 10th & Class 12th'),
)
class_choice = (
    ('Select', 'Select'),
	('Class 10th', 'Class 10th'),
	('Class 12th', 'Class 12th'),
)
paid_choice = (
    ('Select', 'Select'),
	('Paid', 'Paid'),
	('Unpaid', 'Unpaid'),
)
class UserOTP(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	time_st = models.DateTimeField(auto_now = True)
	otp = models.SmallIntegerField(default=0)

	def __str__(self):
		return str(self.user)

class Scribe(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	sc_st = models.CharField(max_length=13, default = "Scribe")
	age = models.IntegerField("Your Age",null=True)
	phone = models.BigIntegerField("Your Phone Number",null=True)
	qualification = models.CharField("Highest Qualification",max_length=40, default = "")
	qual_course = models.CharField("Highest Qualification Course:",max_length=40, default = "")
	location = models.CharField("Your Address:",max_length=40, default = "")
	pincode = models.BigIntegerField("Your Pincode:",null=True)
	lang1 = models.CharField("Preferred Language 1:",max_length=40, default = "")
	lang2 = models.CharField("Preferred Language 2:",max_length=40, default = "", blank=True)
	lang3 = models.CharField("Preferred Language 3:",max_length=40, default = "", blank=True)
	classes = models.CharField("Classes you want to write for:",max_length=40, default = "", choices= classes_choice)
	course = models.CharField("Courses you want to write for: (For multiple courses, separate with commas. Ex: English, Maths)",max_length=40, default = "")
	paid_unpaid = models.CharField("Type of Service preferred: Paid or Unpaid",max_length=40, default = "", choices= paid_choice)

	def __str__(self):
		return str(self.user)

class Student(models.Model):
	user = models.ForeignKey(User, on_delete = models.CASCADE)
	sc_st = models.CharField(max_length=13, default = "Student")
	age = models.IntegerField("Your Age:",null=True)
	phone = models.BigIntegerField("Your Phone Number:",null=True)
	disability = models.CharField("Disability:",max_length=40, default = "")
	classes = models.CharField("Your Class:",max_length=40, default="", choices= class_choice)
	course = models.CharField("Courses in your curriculum: (For multiple courses, separate with commas. Ex: English, Maths)",max_length=40, default="")
	lang = models.CharField("Languages Known: (For multiple languages, separate with commas. Ex: English, Hindi)",max_length=40, default="")
	pref_lang = models.CharField("Preferred Instruction Language",max_length=40, default="")
	school = models.CharField("Your School",max_length=40, default = "")
	paid_unpaid = models.CharField("Type of Service preferred: Paid or Unpaid",max_length=40, default="", choices= paid_choice)
	location = models.CharField("Your Address:",max_length=40, default = "")
	pincode = models.BigIntegerField("Your Pincode:",null=True)

	def __str__(self):
		return str(self.user)


# Create your models here.
