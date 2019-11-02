from django .urls import path
from . import views
from django.views.generic import TemplateView

app_name = 'authentication'

urlpatterns = [

    path('register/', views.SignUp.as_view(), name='register'),
    path('sign_in/', views.LoginView.as_view(), name='sign_in'),
    path('profile/', views.profile, name='profile'),

    path('logout/', views.logout, name='logout'),

   ]