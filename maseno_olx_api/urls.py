from django.urls import path, include
from .viewsets import RegistrationAPIView, LoginAPIView
from django.conf import settings

urlpatterns = [
    path('sign-up/', RegistrationAPIView.as_view()),
	 path('login/', LoginAPIView.as_view())
]

