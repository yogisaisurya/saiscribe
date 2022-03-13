from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from . models import Scribe, Student
from django.core.exceptions import ValidationError

class SignUpForm(UserCreationForm):
    name = forms.CharField(label=("Full Name"))
    username = forms.EmailField(label=("Email"))
    phone = forms.IntegerField(label=("Phone Number"))
    class Meta:
        model = User
        fields = ('name', 'username', 'phone', 'password1', 'password2')

class RegisterSc(forms.ModelForm):
    phone = forms.IntegerField(label=("Phone Number"))
    age = forms.IntegerField(label=("Your Age"))
    qualification = forms.CharField(label=("Highest qualification"))
    qual_course = forms.CharField(label=("Qualification course"))
    location = forms.CharField(label=("Permanant address"))
    pincode = forms.IntegerField(label=("Pincode"))
    lang1 = forms.CharField(label=("Preffered Language 1"))
    lang2 = forms.CharField(label=("Preffered Language 2"))
    lang3 = forms.CharField(label=("Preffered Language 3"))
    classes = forms.CharField(label=("Preffered class"))
    course = forms.CharField(label=("Preffered course"))
    paid_unpaid = forms.CharField(label=("Service type"))

    class Meta:
        model = Scribe
        fields = ('phone','age', 'qualification', 'qual_course', 'location', 'pincode', 'lang1', 'lang2', 'lang3', 'classes', 'course', 'paid_unpaid')

class RegisterSt(forms.ModelForm):
    phone = forms.IntegerField(label=("Phone Number"))
    age = forms.IntegerField(label=("Your Age"))
    disability = forms.CharField(label=("Disability"))
    classes = forms.CharField(label=("Class"))
    course = forms.CharField(label=("Courses"))
    lang = forms.CharField(label=("Languages Known"))
    pref_lang = forms.CharField(label=("Preffered Instruction Language"))
    school = forms.CharField(label=("Your School"))
    paid_unpaid = forms.CharField(label=("Service type"))
    location = forms.CharField(label=("Permanant address"))
    pincode = forms.IntegerField(label=("Pincode"))

    class Meta:
        model = Student
        fields = ('phone','age', 'disability', 'classes', 'course', 'lang', 'pref_lang', 'school', 'paid_unpaid', 'location', 'pincode')