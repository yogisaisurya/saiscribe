from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import SignUpForm, RegisterSc, RegisterSt, UpdateSc
from django.contrib.auth.models import User
from django.contrib import messages
import random
from .models import UserOTP, Scribe, Student
from django.conf import settings
from django.core.mail import send_mail
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login
from django.views.generic.edit import UpdateView, DeleteView


usr = None
# Create your views here.



def sc(request):
    global usr
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()

                messages.success(request, f'Account is Created For {usr.username}')


                return redirect('sc1')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'main/sc.html', {'otp': True, 'usr': usr})

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')

            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = name[0]
            if len(name) > 1:
                usr.last_name = name[1]
            usr.is_active = False
            usr.save()
            usr_otp = random.randint(1000, 9999)
            UserOTP.objects.create(user=usr, otp=usr_otp)

            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to Saiscribe.in - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )

        return render(request, 'main/sc.html', {'otp': True, 'usr': usr})
    else:
        form = SignUpForm()

    return render(request, 'main/sc.html', {'form': form})

def st(request):
    global usr
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()

                messages.success(request, f'Account is Created For {usr.username}')


                return redirect('st1')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'main/st.html', {'otp': True, 'usr': usr})

        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            name = form.cleaned_data.get('name').split(' ')

            usr = User.objects.get(username=username)
            usr.email = username
            usr.first_name = name[0]
            if len(name) > 1:
                usr.last_name = name[1]
            usr.is_active = False
            usr.save()
            usr_otp = random.randint(1000, 9999)
            UserOTP.objects.create(user=usr, otp=usr_otp)

            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to Saiscribe.in - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )

        return render(request, 'main/st.html', {'otp': True, 'usr': usr})
    else:
        form = SignUpForm()

    return render(request, 'main/st.html', {'form': form})


def login_view(request):
    global usr
    if request.user.is_authenticated:
        return redirect('home')
    if request.method == 'POST':
        get_otp = request.POST.get('otp')

        if get_otp:
            get_usr = request.POST.get('usr')
            usr = User.objects.get(username=get_usr)
            if int(get_otp) == UserOTP.objects.filter(user=usr).last().otp:
                usr.is_active = True
                usr.save()
                login(request, usr)
                return redirect('home')
            else:
                messages.warning(request, f'You Entered a Wrong OTP')
                return render(request, 'main/login.html', {'otp': True, 'usr': usr})

        usrname = request.POST['username']
        passwd = request.POST['password']

        user = authenticate(request, username=usrname, password=passwd)  # None
        if user is not None:
            login(request, user)
            return redirect('home')
        elif not User.objects.filter(username=usrname).exists():
            messages.warning(request,
                             f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')
        elif not User.objects.get(username=usrname).is_active:
            usr = User.objects.get(username=usrname)
            usr_otp = random.randint(1000, 9999)
            UserOTP.objects.create(user=usr, otp=usr_otp)
            mess = f"Hello {usr.first_name},\nYour OTP is {usr_otp}\nThanks!"

            send_mail(
                "Welcome to Saiscribe.in - Verify Your Email",
                mess,
                settings.EMAIL_HOST_USER,
                [usr.email],
                fail_silently=False
            )
            return render(request, 'main/login.html', {'otp': True, 'usr': usr})
        else:
            messages.warning(request,
                             f'Please enter a correct username and password. Note that both fields may be case-sensitive.')
            return redirect('login')

    form = AuthenticationForm()
    return render(request, 'main/login.html', {'form': form})


def sc1(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterSc(request.POST)
        if form.is_valid():
            scribe_form = form.save(commit=False)
            scribe_form.user = User.objects.get(username= usr)
            scribe_form.save()
            return redirect('login')
    else:
        form = RegisterSc()

    return render(request, 'main/sc1.html', {'form': form})

def st1(request, *args, **kwargs):
    if request.method == 'POST':
        form = RegisterSt(request.POST)
        if form.is_valid():
            student_form = form.save(commit=False)
            student_form.user = User.objects.get(username= usr)
            student_form.save()
            return redirect('login')
    else:
        form = RegisterSt()

    return render(request, 'main/st1.html', {'form': form})


def home(request):
    if request.user.is_authenticated:
        user = User.objects.get(username= request.user)
        if not Student.objects.filter(user = user):
            detail = Scribe.objects.get(user = user)
        else:
            detail = Student.objects.get(user = user)
        context = {
            'user' : user,
            'detail' : detail
             }
        return render(request, 'main/index.html', context)
    return render(request, 'main/index.html')

def prof(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            user = User.objects.get(username=request.user)
            if not Student.objects.filter(user=user):
                detail = Scribe.objects.get(user=user)
                form = RegisterSc(request.POST, instance=detail)
            else:
                detail = Student.objects.get(user=user)
                form = RegisterSt(request.POST, instance= detail)
            if form.is_valid():
                form.save()
                return redirect('home')
        else:
            user = User.objects.get(username=request.user)
            if not Student.objects.filter(user=user):
                detail = Scribe.objects.get(user=user)
                form = RegisterSc(instance=detail)
            else:
                detail = Student.objects.get(user=user)
                form = RegisterSt(instance= detail)
        return render(request, 'main/prof.html', {'form': form})
    else:
        return redirect('home')
    return render(request, 'main/prof.html')

def about(request):
    return render(request, 'main/about.html')