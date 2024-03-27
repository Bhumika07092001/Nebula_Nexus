from django.urls import path
from .views import RegistrationAPIView, VerificationAPIView, LoginAPIView, ForgotPasswordAPIView, ResetPasswordAPIView

urlpatterns = [
    path('register/', RegistrationAPIView.as_view(), name='register'),
    path('verify/', VerificationAPIView.as_view(), name='verify'),
    path('login/', LoginAPIView.as_view(), name='login'),
    path('forgot-password/', ForgotPasswordAPIView.as_view(), name='forgot_password'),
    path('reset-password/', ResetPasswordAPIView.as_view(), name='reset_password'),

]
