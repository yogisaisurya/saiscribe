from django.urls import path, include
from .views import home, sc, login_view, sc1, st, st1, prof, about
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', home, name= 'home'),
    path('prof/', prof, name= 'prof'),
    path('about/', about, name= 'about'),
    path('sc/', sc, name= 'sc'),
    path('st/', st, name= 'st'),
    path('sc1/', sc1, name='sc1'),
    path('st1/', st1, name='st1'),
    path('login/', login_view, name = 'login'),
    #path('login/', LoginView.as_view(template_name= 'main/login.html', redirect_authenticated_user =True ), name= 'login'),
    path('logout/', LogoutView.as_view(next_page = 'home'), name='logout'),
    
    path("password-reset/", auth_views.PasswordResetView.as_view(template_name='main/password_reset.html'), name="password_reset"),

    path("password-reset-done/", auth_views.PasswordResetDoneView.as_view(template_name='main/pass_reset_done.html'), name="password_reset_done"),

    path("password-reset-confirm/<uidb64>/<token>/", auth_views.PasswordResetConfirmView.as_view(template_name='main/password_reset_confirm.html'), name="password_reset_confirm"),

    path("password-reset-complete/", auth_views.PasswordResetCompleteView.as_view(template_name='main/password_reset_complete.html'), name="password_reset_complete"),

]